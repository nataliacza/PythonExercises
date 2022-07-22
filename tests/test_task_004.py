import unittest
from challenges.task_004 import swap_elements, swap_elements_2

list_nr1 = [4, 5, 6, 7]  # [7, 5, 6, 4]
list_nr2 = [4, 5, 6, 7, 1]  # [1, 5, 6, 7, 4]
list_nr3 = [4, 5]  # [5, 4]


class TestOfSwapFunctionOne(unittest.TestCase):

    def test_function_1(self):
        result = swap_elements(list_nr1)
        expected = [7, 5, 6, 4]
        self.assertEqual(result, expected)

    def test_function_2(self):
        result = swap_elements(list_nr2)
        expected = [1, 5, 6, 7, 4]
        self.assertEqual(result, expected)

    def test_function_3(self):
        result = swap_elements(list_nr3)
        expected = [5, 4]
        self.assertEqual(result, expected)


class TestOfSwapFunctionTwo(unittest.TestCase):

    def test_function_1(self):
        result = swap_elements_2(list_nr1)
        expected = [7, 5, 6, 4]
        self.assertEqual(result, expected)

    def test_function_2(self):
        result = swap_elements_2(list_nr2)
        expected = [1, 5, 6, 7, 4]
        self.assertEqual(result, expected)

    def test_function_3(self):
        result = swap_elements_2(list_nr3)
        expected = [5, 4]
        self.assertEqual(result, expected)
