"""Константы для jim протокола, настройки"""
# Ключи
ACTION = 'action'
TIME = 'time'
USER = 'user'
ACCOUNT_NAME = 'account_name'
RESPONSE = 'response'
ERROR = 'error'
ALERT = 'alert'

# Значения
PRESENCE = 'presence'
MSG = 'msg'
FROM = 'from'
TO = 'to'
MESSAGE = 'message'

# Коды ответов (будут дополняться)
BASIC_NOTICE = 100
OK = 200
ACCEPTED = 202
WRONG_REQUEST = 400  # неправильный запрос/json объект
SERVER_ERROR = 500

# Кортеж из кодов ответов
RESPONSE_CODES = (BASIC_NOTICE, OK, ACCEPTED, WRONG_REQUEST, SERVER_ERROR)
ACTIONS = (PRESENCE, MSG)
