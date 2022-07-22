import unittest
from challenges.task_003 import is_valid_array, is_valid_array_2

list_nr1 = [[3], [4]]
list_nr2 = [[3, 4], [4, 5]]
list_nr3 = [[3, 4, 5], [4, 5]]
list_nr4 = [[[]]]


class TestOfValidArrayFunctionOne(unittest.TestCase):

    def test_function_1(self):
        result = is_valid_array(list_nr1)
        self.assertTrue(result)

    def test_function_2(self):
        result = is_valid_array(list_nr2)
        self.assertTrue(result)

    def test_function_3(self):
        result = is_valid_array(list_nr3)
        self.assertFalse(result)

    def test_function_4(self):
        result = is_valid_array(list_nr4)
        self.assertTrue(result)


class TestOfValidArrayFunctionTwo(unittest.TestCase):

    def test_function_1(self):
        result = is_valid_array_2(list_nr1)
        self.assertTrue(result)

    def test_function_2(self):
        result = is_valid_array_2(list_nr2)
        self.assertTrue(result)

    def test_function_3(self):
        result = is_valid_array_2(list_nr3)
        self.assertFalse(result)

    def test_function_4(self):
        result = is_valid_array_2(list_nr4)
        self.assertTrue(result)
