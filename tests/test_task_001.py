import unittest
from challenges.task_001 import is_nested, is_nested_2, is_nested_3, is_nested_4

list_nr1 = []
list_nr2 = [[2, 3], [5, 5]]
list_nr3 = [[1, 2], 4]
list_nr4 = [[1, 2], (0,)]


class TestOfNestedFunctionOne(unittest.TestCase):

    def test_function_1(self):
        result = is_nested(list_nr1)
        self.assertFalse(result)

    def test_function_2(self):
        result = is_nested(list_nr2)
        self.assertTrue(result)

    def test_function_3(self):
        result = is_nested(list_nr3)
        self.assertFalse(result)

    def test_function_4(self):
        result = is_nested(list_nr4)
        self.assertFalse(result)


class TestOfNestedFunctionTwo(unittest.TestCase):

    def test_function_1(self):
        result = is_nested_2(list_nr1)
        self.assertFalse(result)

    def test_function_2(self):
        result = is_nested_2(list_nr2)
        self.assertTrue(result)

    def test_function_3(self):
        result = is_nested_2(list_nr3)
        self.assertFalse(result)

    def test_function_4(self):
        result = is_nested_2(list_nr4)
        self.assertFalse(result)


class TestOfNestedFunctionThree(unittest.TestCase):

    def test_function_1(self):
        result = is_nested_3(list_nr1)
        self.assertFalse(result)

    def test_function_2(self):
        result = is_nested_3(list_nr2)
        self.assertTrue(result)

    def test_function_3(self):
        result = is_nested_3(list_nr3)
        self.assertFalse(result)

    def test_function_4(self):
        result = is_nested_3(list_nr4)
        self.assertFalse(result)


class TestOfNestedFunctionFour(unittest.TestCase):

    def test_function_1(self):
        result = is_nested_4(list_nr1)
        self.assertFalse(result)

    def test_function_2(self):
        result = is_nested_4(list_nr2)
        self.assertTrue(result)

    def test_function_3(self):
        result = is_nested_4(list_nr3)
        self.assertFalse(result)

    def test_function_4(self):
        result = is_nested_4(list_nr4)
        self.assertFalse(result)
