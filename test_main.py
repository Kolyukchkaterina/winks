from unittest import TestCase
from main import create_hello_msg, empty_user, users, start, func

class Test(TestCase):
    def test_create_hello_msg(self):
        self.assertEqual(
            'Obc' in create_hello_msg('Obc'),
            True
        )

        self.assertEqual(
            'cringe' in create_hello_msg('Heyman'),
            False
        )


    def test_user_empty(self):
        self.assertEqual(
            123 not in users, True
        )

        temp = empty_user(123)

        self.assertEqual(
            123 in users, True
        )

        self.assertEqual(
            temp['vedma'], 0
        )

    def test_start(self):
        with self.assertRaises(AttributeError):
            start(None)

    def test_handler(self):
        with self.assertRaises(AttributeError):
            func(None)

