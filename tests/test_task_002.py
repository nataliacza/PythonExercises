import unittest
from challenges.task_002 import is_all_equal, is_all_equal_2

list_nr1 = [4, 5, 6]
list_nr2 = [4, 4, 4]
list_nr3 = [4, 4, "4"]
list_nr4 = ["Q", "Q", "Q"]
list_nr5 = ["Q", "Q", "DQ"]


class TestOfEqualFunctionOne(unittest.TestCase):

    def test_function_1(self):
        result = is_all_equal(list_nr1)
        self.assertFalse(result)

    def test_function_2(self):
        result = is_all_equal(list_nr2)
        self.assertTrue(result)

    def test_function_3(self):
        result = is_all_equal(list_nr3)
        self.assertFalse(result)

    def test_function_4(self):
        result = is_all_equal(list_nr4)
        self.assertTrue(result)

    def test_function_5(self):
        result = is_all_equal(list_nr5)
        self.assertFalse(result)


class TestOfNestedFunctionTwo(unittest.TestCase):

    def test_function_1(self):
        result = is_all_equal_2(list_nr1)
        self.assertFalse(result)

    def test_function_2(self):
        result = is_all_equal_2(list_nr2)
        self.assertTrue(result)

    def test_function_3(self):
        result = is_all_equal_2(list_nr3)
        self.assertFalse(result)

    def test_function_4(self):
        result = is_all_equal_2(list_nr4)
        self.assertTrue(result)

    def test_function_5(self):
        result = is_all_equal_2(list_nr5)
        self.assertFalse(result)
