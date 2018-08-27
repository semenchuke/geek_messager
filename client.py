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
from jim.jim_main import JimPresence, JimMessage, Jim, JimResponse

class User:
    def __init__(self, username):
        self.username = username

    def create_presence(self):
        jim_presence = JimPresence(self.username)
        message = jim_presence.to_dict()
        return message

    def look_at_response(self, response):
        result = Jim.from_dict(response)
        return result.to_dict()

    def create_message(self, message_to, text):
        message = JimMessage(message_to, self.username, text)
        message.to_dict()

    def read_messages(self, sock):
        while True:
            print('читаю')
            jim_message = get_message(sock)
            print(jim_message)
            print(jim_message[MESSAGE])

    def write_messages(self, sock):
        while True:
            text = input('>> Отправить: ')
            jim_message = self.create_message('#all', text)
            send_message(sock, jim_message)


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
    try:
        mode = sys.argv[3]
    except IndexError:
        mode = 'r'
    # Соединиться с сервером
    client.connect((addr, port))
    # создаем пользователя
    user = User('Nick Strong')
    # Создаем сообщение
    presence = user.create_presence()
    # Отсылаем сообщение
    send_message(client, presence)
    # Получаем ответ
    response = get_message(client)
    # Проверяем ответ
    response = user.look_at_response(response)
    if response[RESPONSE] == OK:
        if mode == 'r':
            user.read_messages(client)
        elif mode == 'w':
            user.write_messages(client)
        else:
            raise Exception('Неверный режим чтения / записи')
