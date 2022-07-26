import unittest
from challenges.task_015 import filter_users, filter_users_2, filter_users_3

list1 = [
    {"user_id": "3546", "level": 64, "is_active": True},
    {"user_id": "3467", "level": 34, "is_active": False},
    {"user_id": "6676", "is_active": True},
    {"user_id": "8454", "level": 1, "is_active": False},
    {"user_id": "5511", "is_active": False}
]

expected1 = [
    {"user_id": "3546", "level": 64, "is_active": True},
    {"user_id": "3467", "level": 34, "is_active": False},
    {"user_id": "8454", "level": 1, "is_active": False},
]

class TestOfFilterFunctionOne(unittest.TestCase):

    def test_function_1(self):
        result = filter_users(list1)
        expected = expected1
        self.assertEqual(result, expected)


class TestOfFilterFunctionTwo(unittest.TestCase):

    def test_function_1(self):
        result = filter_users_2(list1)
        expected = expected1
        self.assertEqual(result, expected)


class TestOfFilterFunctionThree(unittest.TestCase):

    def test_function_1(self):
        result = filter_users_3(list1)
        expected = expected1
        self.assertEqual(result, expected)
