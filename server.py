"""
Функции ​​сервера:​
- принимает ​с​ообщение ​к​лиента;
- формирует ​​ответ ​к​лиенту;
- отправляет ​​ответ ​к​лиенту;
- имеет ​​параметры ​к​омандной ​с​троки:
- -p ​​<port> ​-​ ​​TCP-порт ​​для ​​работы ​(​по ​у​молчанию ​​использует ​​порт ​​7777);
- -a ​​<addr> ​-​ ​I​P-адрес ​​для ​​прослушивания ​(​по ​у​молчанию ​с​лушает ​​все ​​доступные ​​адреса).
"""

import sys
import json
from socket import socket, AF_INET, SOCK_STREAM
from jim.utils import dict_to_bytes, bytes_to_dict, send_message, get_message
from jim.config import *

def presence_response(presence_message):
    """
    формирование ответа клиенту по его сообощению
    :param presence_message: словарь (presence) запроса клиента
    :return: словарь ответа
    """
    #проверяем что нам пришло presence сообщение
    #если все ок, шлёи код ответа 200 иначе 400

    if ACTION in presence_message and \
            presence_message[ACTION] == PRESENCE and \
            TIME in presence_message and \
            isinstance(presence_message[TIME], float):
        return {RESPONSE: 200}
    else:
        return {RESPONSE: 400, ERROR: 'был получен не верный запрос'}


if __name__ == '__main__':
    server = socket(AF_INET, SOCK_STREAM)

    try:
        addr = sys.argv[1]
    except IndexError:
        addr = 'localhost'
    try:
        port = sys.argv[2]
    except IndexError:
        port = 7777
    except ValueError:
        print('Номер порта должен быть целым числом')
        sys.exit(0)

    server.bind((addr, port))
    server.listen(10)
    while True:
        client, addr = server.accept()
        #получаем сообщение от клиента
        presence = get_message(client)
        #печатаем сообщение
        print(presence)

        #формируем ответ и отсылаем его
        responce = presence_response(presence)
        send_message(client, responce)
        client.close()

