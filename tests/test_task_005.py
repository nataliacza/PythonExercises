import unittest
from challenges.task_005 import swap_elements

list_nr1 = [4, 5, 6, 7, 1]
list_nr2 = ["a", "b", "c", "d", "e"]
list_nr3 = [2.1, 5.2, 6.2, 7.1, 2.6, 2.1]


class TestOfSwapFunctionOne(unittest.TestCase):

    def test_function_1(self):
        result = swap_elements(list_nr1, 1, 2)
        expected = [4, 6, 5, 7, 1]
        self.assertEqual(result, expected)

    def test_function_2(self):
        result = swap_elements(list_nr2, 4, 2)
        expected = ["a", "b", "e", "d", "c"]
        self.assertEqual(result, expected)

    def test_function_3(self):
        result = swap_elements(list_nr3, 3, 2)
        expected = [2.1, 5.2, 7.1, 6.2, 2.6, 2.1]
        self.assertEqual(result, expected)
