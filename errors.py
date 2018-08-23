"""Создадим здесь свои исключения"""

class UserNameToLongError(Exception):
    def __init__(self, username):
        self.username = username

    def __str__(self):
        return 'Имя пользователя {} не должно превышать 26 символов'.format(self.username)


class ResponseCodeError(Exception):
    def __init__(self, code):
        self.code = code

    def __str__(self):
        return 'Неверный код ответа'.format(self.code)


class ResponseCodeLenError(Exception):
    def __init__(self, code):
        self.codelen = len(code)

    def __str__(self):
        return 'Неверная длина кода {}, длина кода должна равняться 3 символам'.format(self.codelen)
    

class MandatoryKeyError(Exception):
    def ___init__(self, key):
        self.key = key

    def __str__(self):
        return 'Нет обязательного атрибута {}'.format(self.key)