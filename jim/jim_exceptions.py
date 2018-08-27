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
