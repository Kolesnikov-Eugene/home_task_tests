from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

URL = 'https://passport.yandex.ru/auth/'
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

driver.maximize_window()
driver.get(URL)

user_login = driver.find_element(By.NAME, 'login')
user_login.send_keys('Vasya@mail.ru')
submit_button = driver.find_element(By.ID, 'passp:sign-in')
submit_button.click()
time.sleep(100)
response = driver.find_element(By.CLASS_NAME, 'passp-title')
mes = 'Мы отправили письмо'
assert 'Мы отправили письмо' in response.text
driver.quit()
