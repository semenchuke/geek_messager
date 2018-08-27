import time as ctime
from .config import *
from .jim_exceptions import WrongParamError, WrongActionError, WrongDictError


class Jim:
    # основной родительский метод
    def to_dict(self):
        return {}

    # метод создания классов на основе Jim
    @staticmethod
    def try_create(jim_class, input_dict):
        try:
            return jim_class(**input_dict)
        except KeyError:
            raise WrongParamError(input_dict)

    @staticmethod
    def from_dict(input_dict):
        """
        метод создания класса из входного словаря,
        в соответствии с параметром ACTION
        :param input_dict: входной словарь
        :return: jim-объект
        """
        if ACTION in input_dict:
            action = input_dict.pop(ACTION)

            if action in ACTIONS:
                if action == PRESENCE:
                    return Jim.try_create(JimPresence, input_dict)
                elif action == MSG:
                    try:
                        input_dict['from_'] = input_dict['from']
                    except KeyError:
                        return WrongParamError(input_dict)
                    del input_dict['from']
                    return Jim.try_create(JimMessage, input_dict)
            else:
                raise WrongActionError(action)
        elif RESPONSE in input_dict:
            return Jim.try_create(JimResponse, input_dict)
        else:
            raise WrongDictError(input_dict)


class JimAction(Jim):
    def __init__(self, action, time=None):
        self.action = action
        if time:
            self.time = time
        else:
            self.time = ctime.time()

    def to_dict(self):
        result = super().to_dict()
        result[ACTION] = self.action
        result[TIME] = self.time
        return result

class JimPresence(JimAction):
    def __init__(self, account_name, time):
        self.account_name = account_name
        super().__init__(PRESENCE, time)

    def to_dict(self):
        result = super().to_dict()
        result[ACCOUNT_NAME] = self.account_name
        return result

class JimMessage(JimAction):
    message = 'message'

    def __init__(self, to, from_, message, time=None):
        self.to = to
        self.from_ = from_
        self.message = message
        super().__init__(MSG, time)

    def to_dict(self):
        result = super().to_dict()
        result[TO] = self.to
        result[FROM] = self.from_
        result[MESSAGE] = self.message
        return result

class JimResponse(JimAction):
    response = 'response'

    def __init__(self, response, error=None, alert=None):
        self.response = response
        self.error = error
        self.alert = alert

    def to_dict(self):
        result = super().to_dict()
        result[RESPONSE] = self.response
        if self.error:
            result[ERROR] = self.error
        if self.alert:
            result[ALERT] = self.alert
        return result






