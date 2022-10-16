import unittest
from yandex_api import create_folder, delete_folder


class TestYandexApi(unittest.TestCase):
    response = 201
    def setUp(self) -> None:
        print('beginning')

    def tearDown(self) -> None:
        delete_folder('new')

    def test_yandex_api(self):
        result = create_folder('new')
        self.assertEqual(result, self.response)


if __name__ == '__main__':
    unittest.main()