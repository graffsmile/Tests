import unittest
from os.path import exists
from unittest import TestCase
from API_Yandex import *


class TestYD(TestCase):
    # @unittest.skip('skip')
    def test_api_yandex(self):
        """
        Тест функции создания папки на Яндекс.Диске
        """
        print('method "test_api_yandex"')
        self.assertEqual(folder_creation('test_api'), 201)


    # @unittest.skip
    def test_yd_pass(self):
        if folder_creation('test') is not exists:
            print('method "test_yd_pass"')
            self.assertEqual(folder_creation('test'), 409)
        else:
            self.assertEqual(folder_creation('test'), 201)
            print(folder_creation('test'))

    # @unittest.skip('Пропускаем метод "tearDown"')
    def tearDown(self):
        delete_folder('test_api')
        delete_folder('test')
        delete_folder('test_1')

    # @unittest.skip
    def test_yd(self):
        for i, (path, expected) in enumerate((
                ('test_1', 201),
                ('test_1', 409)
        )):
            with self.subTest(i):
                print('method "test_yd"')
                result = folder_creation(path)
                self.assertEqual(expected, result)
