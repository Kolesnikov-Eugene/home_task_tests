import requests
from pathlib import Path

URL = 'https://cloud-api.yandex.net/v1/disk/resources'
dir_path = Path.home()

full_path = Path(dir_path, 'Учеба/python_home_tasks/advanced/home_task_tests/token.txt')
TOKEN = open(full_path).read()

def create_folder(path):
    params = {'path': path}
    headers = {'Content-Type': 'application/json',
               'Authorization': TOKEN}
    create_dir = requests.put(URL, headers=headers, params=params)
    return create_dir.status_code

def delete_folder(path):
    params = {'path': path}
    headers = {'Content-Type': 'application/json',
               'Authorization': TOKEN}
    dir_ = requests.delete(URL, headers=headers, params=params)
    return dir_.status_code

if __name__ == '__main__':
    create_folder('new')
    delete_folder('new')