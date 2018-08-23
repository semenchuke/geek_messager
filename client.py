"""
Функции ​к​лиента:​
- сформировать ​​presence-сообщение;
- отправить ​с​ообщение ​с​ерверу;
- получить ​​ответ ​с​ервера;
- разобрать ​с​ообщение ​с​ервера;
- параметры ​к​омандной ​с​троки ​с​крипта ​c​lient.py ​​<addr> ​[​<port>]:
- addr ​-​ ​i​p-адрес ​с​ервера;
- port ​-​ ​t​cp-порт ​​на ​с​ервере, ​​по ​у​молчанию ​​7777.
"""
import sys
import time
from socket import socket, AF_INET, SOCK_STREAM
from errors import UserNameToLongError, ResponseCodeLenError, MandatoryKeyError, ResponseCodeError
from jim.config import *
from jim.utils import send_message, get_message


def create_presence(account_name="Guest"):
    """
    Сформировать ​​presence-сообщение
    :param account_name: Имя пользователя
    :return: Словарь сообщения
    tests:
    ИЗ-ЗА времени трудно написать doctest
    """
    # Если имя не строка
    if not isinstance(account_name, str):
        # Генерируем ошибку передан неверный тип
        raise TypeError
    # Если длина имени пользователя больше 25 символов
    if len(account_name) > 26:
        # генерируем нашу ошибку имя пользователя слишком длинное
        raise UserNameToLongError(account_name)
    # формируем словарь сообщения
    message = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: account_name
        }
    }
    # возвращаем
    return message


def translate_message(response):
    """
    Разбор сообщения
    :param response: Словарь ответа от сервера
    :return: корректный словарь ответа
    """
    # Передали не словарь
    if not isinstance(response, dict):
        raise TypeError
    # Нету ключа response
    if RESPONSE not in response:
        # Ошибка нужен обязательный ключ
        raise MandatoryKeyError(RESPONSE)
    # получаем код ответа
    code = response[RESPONSE]
    # длина кода не 3 символа
    if len(str(code)) != 3:
        # Ошибка неверная длина кода ошибки
        raise ResponseCodeLenError(code)
    # неправильные коды символов
    if code not in RESPONSE_CODES:
        # ошибка неверный код ответа
        raise ResponseCodeError(code)
    # возвращаем ответ
    return response


if __name__ == '__main__':
    client = socket(AF_INET, SOCK_STREAM)  # Создать сокет TCP
    # Пытаемся получить параметры скрипта
    try:
        addr = sys.argv[1]
    except IndexError:
        addr = 'localhost'
    try:
        port = int(sys.argv[2])
    except IndexError:
        port = 7777
    except ValueError:
        print('Порт должен быть целым числом')
        sys.exit(0)
    # Соединиться с сервером
    client.connect((addr, port))
    # Создаем сообщение
    presence = create_presence('Nick Strong')
    # Отсылаем сообщение
    send_message(client, presence)
    # Получаем ответ
    response = get_message(client)
    # Проверяем ответ
    response = translate_message(response)
    print(response)
