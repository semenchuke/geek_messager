class WrongParamError(Exception):
    def __init__(self, input_params):
        self.inpit_params = input_params

    def __str__(self):
        return 'Wrong input params {}'.format(self.inpit_params)

class WrongActionError(Exception):
    def __init__(self, input_action):
        self.input_action = input_action

    def __str__(self):
        return 'There is no action in ACTIONS like {}'.format(self.input_action)

class WrongDictError(Exception):
    def __init__(self, input_dict):
        self.input_dict = input_dict

    def __str__(self):
        return 'Wrong input dict {}'.format(self.input_dict)


class ToLongError(Exception):
    """Ошибка когда наше поле длинее чем надо"""

    def __init__(self, name, value, max_length):
        """
        :param name: имя поля
        :param value: текущее значение
        :param max_length: максимальное значение
        """
        self.name = name
        self.value = value
        self.max_length = max_length

    def __str__(self):
        return '{}: {} to long (> {} simbols)'.format(self.name, self.value, self.max_length)


class ResponseCodeError(Exception):
    def __init__(self, code):
        self.code = code

    def __str__(self):
        return 'Wrong response code: {}'.format(self.code)