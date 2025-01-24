def check_auth(login: str, password: str):
    """
    Проверка логина и пароля
    """
    if login == 'admin' and password == 'password':
        result = "Добро пожаловать"
    else:
        result = "Доступ ограничен"
    return result

def check_email(email: str) -> bool:
    """
    Проверка email
    """
    if '@' in email and '.' in email and ' ' not in email:
        result = True
    else:
        result = False
    return result


def discriminant(a, b, c):
    """
    функция для нахождения дискриминанта
    """
    return b ** 2 - 4 * a * c

def solution(a, b, c):
    """
    функция для нахождения корней уравнения
    """
    if discriminant (a, b, c) < 0:
        return "корней нет"
    elif discriminant (a, b, c) == 0:
        x = -b / (2 * a)
        return (x)
    elif discriminant (a, b, c) > 0:
        x_1 = -b / 2 + discriminant(a, b, c) ** 0.5 / 2 * a
        x_2 = -b / 2 - discriminant(a, b, c) ** 0.5 / 2 * a
        return (x_1, x_2)
