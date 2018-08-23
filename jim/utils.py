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