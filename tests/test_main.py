import unittest
from unittest import TestCase
from functions import *


class TestMain(TestCase):
    def test_auth_1(self):
        """
        Тест для функции проверки логина и пароля
        """
        login = 'admin'
        password = 'password'
        espected = 'Добро пожаловать'
        result = check_auth('admin', 'password')
        self.assertEqual(espected, result)

    @unittest.expectedFailure
    def test_auth_2(self):
        login = 'admin'
        password = 'password'
        espected = 'Добро пожаловать'
        result = check_auth('admin', 123)
        self.assertEqual(espected, result)

    def test_auth_with_params(self):
        """
        Параметризованный тест функции проверки логина и пароля
        """
        for i, (login, password, expected) in enumerate((
                ('админ', 'password', 'Доступ ограничен'),
                ('admin', 'password', 'Добро пожаловать'),
                ('user', 'password', 'Доступ ограничен'),
                ('admin', 123, 'Доступ ограничен')
        )):
            with self.subTest(i):
                result = check_auth(login, password)
                self.assertEqual(expected, result)



    def test_email(self):
        """
        Тест функции проверки email
        """
        espected = True
        result = check_email('helloworld@mail.ru')
        self.assertEqual(espected, result)

    def test_email_with_params(self):
        """
        Параметризованный тест функции проверки email
        """
        for i, (email, expected) in enumerate((
                ('helloworld@mail.ru', True),
                ('helloworld@mailru', False),
                ('hello world@ ya.ru', False),
                ('helloworld_mail.ru', False)
        )):
            with self.subTest(i):
                result = check_email(email)
                self.assertEqual(expected, result)


    def test_discriminant_with_params(self):
        """
        Параметризованный тест функции нахождения корней уравнения
        """
        for i, ((a, b, c), expected) in enumerate((
                ((1, 8, 15), (-3.0, -5.0)),
                ((1, -13, 12), (12, 1)),
                ((-4, 28, -49), 3.5),
                ((1, 1, 1), 'корней нет')
        )):
            with self.subTest(i):
                result = solution(a, b, c)
                self.assertEqual(expected, result)