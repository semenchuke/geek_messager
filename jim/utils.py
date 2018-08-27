import json

ENCODING = 'utf-8'

def dict_to_bytes(jim_message):
    """
    преобразуем какой-либо словарь в байты
    :param message_dict: словарь
    :return: байты
    """
    #проверка входных данных
    if isinstance(jim_message, dict):
        # преобразуем в json
        jim_message_json = json.dumps(jim_message)
        # преобразуем в байты
        byte_jim_message = jim_message_json.encode(ENCODING)
        # перевод осуществлён - возвращаем
        return byte_jim_message
    else:
        raise TypeError

def bytes_to_dict(byte_jim_message):
    """
    преобразуем выражение из байт в словарь
    :param byte_jim_message: байты
    :return: словарь
    """
    # проверка входных данных
    if isinstance(byte_jim_message, bytes):
        # декодируем байты в json
        jim_message_json = byte_jim_message.decode(ENCODING)
        # достаём словарь из json объекта
        jim_message = json.loads(jim_message_json)
        # проверяем реально ли мы достали словарь
        if isinstance(jim_message, dict):
            # проверка прошла успешно - возвращаем объект
            return jim_message
        else:
            # получили не словарь
            return TypeError
    else:
        # получили не байты
        return TypeError

def send_message(sock, jim_message):
    """
    метод передачи сообщения
    :param sock: сокет для передачи
    :param message: сообщений
    :return: None
    """
    # перевели словарь в байты
    byte_message = dict_to_bytes(jim_message)
    # отправили
    sock.send(byte_message)

def get_message(sock):
    """
    метод чтения сообщений
    :param sock: сокет с которого принимаем
    :return: словарь по протоколу jim
    """
    # получаем до 1024 байт
    byte_jim_message = sock.recv(1024)
    # пробуем перевести байты в словарь
    jim_message = bytes_to_dict(byte_jim_message)
    # если все ок возвращаем jim сообщение
    return jim_message