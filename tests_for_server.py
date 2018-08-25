import unittest
import time
from jim.config import *
from server import presence_response


class STest(unittest.TestCase):

    def test_presence_response_ok(self):
        res = presence_response({
            ACTION: PRESENCE,
            TIME: time.time()
        })

        self.assertEqual(res, {RESPONSE: 200,
                MESSAGE: 'Hello client'})

    def test_presence_response_no_action(self):
        res = presence_response({
            'FACTION': PRESENCE,
            TIME: time.time()
        })

        self.assertEqual(res, {RESPONSE: 400, ERROR: 'был получен не верный запрос'})

    def test_presence_response_no_presence(self):
        res = presence_response({
            ACTION: 'fail',
            TIME: time.time()
        })

        self.assertEqual(res, {RESPONSE: 400, ERROR: 'был получен не верный запрос'})

    def test_presence_response_no_time(self):
        res = presence_response({
            ACTION: PRESENCE,
            'MIME': time.time()
        })

        self.assertEqual(res, {RESPONSE: 400, ERROR: 'был получен не верный запрос'})

    def test_presence_response_time_not_float(self):
        res = presence_response({
            ACTION: PRESENCE,
            TIME: 777
        })

        self.assertEqual(res, {RESPONSE: 400, ERROR: 'был получен не верный запрос'})

