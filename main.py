from functions import *


def test_function(func, expected, *args, **kwargs):
    result = func(*args, **kwargs)
    try:
        assert result == expected
        print(f'\033[32mТест {func} с аргументами {args,kwargs} пройден')
    except AssertionError:
        print(f'\033[31mТест {func} с аргументами {args, kwargs} не пройден')


if __name__ == '__main__':
    test_function(check_auth, "Добро пожаловать", 'admin', 'password')
    test_function(check_auth, "Доступ ограничен", 'user', 'password')
    test_function(check_auth, "Добро пожаловать", 'user', 'password')
    test_function(check_email, True,'helloworld@mail.ru')
    test_function(check_email, False,'hello world@ ya.ru')
    test_function(solution, (-3.0, -5.0), 1, b=8, c=15)
    test_function(solution, (12, 1), 1, -13, 12)
    test_function(solution, 3.5, -4, 28, -49)
    test_function(solution, 'корней нет', 1, 1, 1)