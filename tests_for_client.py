import unittest
from jim.config import *
from client import create_presence, translate_message
from errors import *

class CTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_create_presence_all(self):
        #неверный тип
        with self.assertRaises(TypeError):
            create_presence(777)

        with self.assertRaises(TypeError):
            create_presence(None)

        #слишком длинное имя
        with self.assertRaises(UserNameToLongError):
            create_presence('0123456789012345678901234567')

        # запуск функции без параметра
        res = create_presence()
        self.assertEqual(res[USER][ACCOUNT_NAME], 'Guest')

        # запуск с параметром
        res = create_presence('Natali')
        self.assertEqual(res[USER][ACCOUNT_NAME], 'Natali')

    def test_translate_message(self):
        # неверный тип
        with self.assertRaises(TypeError):
            translate_message(777)

        # обязательный ключ response
        with self.assertRaises(MandatoryKeyError):
            translate_message({'a':'b'})

        # неверная длин кода ответа
        with self.assertRaises(ResponseCodeLenError):
            translate_message({'response': '2000'})

        # неверный код ответа
        with self.assertRaises(ResponseCodeError):
            translate_message({'response': 900})
