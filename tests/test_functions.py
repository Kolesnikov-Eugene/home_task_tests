import unittest
from unittest.mock import patch
import main
from main import (reloader, check_document_existance, get_doc_owner_name, get_all_doc_owners_names,
                  remove_doc_from_shelf, delete_doc, add_new_doc)


class TestFuncAccount(unittest.TestCase):
    def setUp(self) -> None:
        print('Before testing')

    def tearDown(self):
        main.reloader()  # reload data after testing

    def test_ckeck_doc_existance(self):
        result = check_document_existance('2207 876234')
        self.assertTrue(result)

    @patch('builtins.input')
    def test_get_doc_owner_name(self, mocked_input):
        mocked_input.return_value = '2207 876234'
        result = get_doc_owner_name()
        self.assertEqual(result, 'Василий Гупкин')

    def test_get_all_doc_owners_names(self):
        result = get_all_doc_owners_names()
        names_list = {'Василий Гупкин', 'Геннадий Покемонов', 'Аристарх Павлов'}
        self.assertEqual(result, names_list)

    def test_remove_doc_from_shelf(self):
        result = remove_doc_from_shelf('11-2')
        self.assertTrue(result)

    @patch('builtins.input')
    def test_delete_doc(self, mocked_input):
        mocked_input.return_value = '11-2'
        result = delete_doc()
        self.assertTrue(result)

    @patch('builtins.input', side_effect=['123', 'pass', 'anns', 4])
    def test_add_new_doc(self, mocked_input):
        result = add_new_doc()
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()