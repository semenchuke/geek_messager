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
import select
from socket import socket, AF_INET, SOCK_STREAM
from jim.utils import send_message, get_message
from jim.config import *
from jim.jim_main import JimResponse, JimMessage, Jim


class Handler:
    """
    основная логика сервера
    """
    def read_requests(self, r_clients, all_clients):
        # список входящих сообщений
        messages = []

        for sock in r_clients:
            try:
                message = get_message(sock)
                messages.append(message)
            except:
                print('Клиент {} {} отключился'. format(sock.fileno(), sock.getpeername()))
                all_clients.remove(sock)

        return messages

    def write_responses(self, messages, w_clients, all_clients):
        for sock in w_clients:
            for message in messages:
                try:
                    send_message(sock, message)
                except:
                    print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpername()))
                    sock.close()
                    all_clients.remove(sock)

    def presence_response(self, jim_message):
        try:
            Jim.from_dict(jim_message)
        except Exception as e:
            response = JimResponse(400, error=str(e))
            return response.to_dict()
        else:
            response = JimResponse(200)
            return response.to_dict()


class Server:
    def __init__(self, handler):
        self.handler = handler
        self.clients = []
        self.sock = socket(AF_INET, SOCK_STREAM)

    def bind(self, addr, port):
        self.sock.bind((addr, port))

    def listen_forever(self):
        self.sock.listen(15)
        self.sock.settimeout(0.2)

        while True:
            try:
                client, addr = self.sock.accept()
                presence = get_message(client)
                print('вот что пришло на сервер ->', presence)
                response = self.handler.presence_response(presence)
                print('вот что отдаём с сервера ->', response)
                send_message(client, response)
            except OSError as e:
                pass
            else:
                print('Получен запрос на соединение от клиента с адресом {}'.format(str(addr)))
                self.clients.append(client)
            finally:
                wait = 0
                r = []
                w = []
                try:
                    r, w, e = select.select(self.clients, self.clients, [], wait)
                except:
                    pass

                requests = self.handler.read_requests(r, self.clients)
                self.handler.write_responses(requests, w, self.clients)




if __name__ == '__main__':
    try:
        addr = sys.argv[1]
    except IndexError:
        addr = ''
    try:
        port = int(sys.argv[2])
    except IndexError:
        port = 7777
    except ValueError:
        print('Порт должен быть целым числом')
        sys.exit(0)

    handler = Handler()
    server = Server(handler)
    server.bind(addr, port)
    server.listen_forever()
