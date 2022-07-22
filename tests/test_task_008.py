import unittest
from challenges.task_008 import get_indices, get_indices_2, get_indices_3

list1 = [4, 3, 5, 2]
searched1 = 2
# [3]

list2 = ["Q", "DQ", "DQ", "DQ", "Q", "Q"]
searched2 = "Q"
# [0, 4, 5]

class TestOfSearchFunctionOne(unittest.TestCase):

    def test_function_1(self):
        result = get_indices(list1, searched1)
        expected = [3]
        self.assertEqual(result, expected)

    def test_function_2(self):
        result = get_indices(list2, searched2)
        expected = [0, 4, 5]
        self.assertEqual(result, expected)


class TestOfSearchFunctionTwo(unittest.TestCase):

    def test_function_1(self):
        result = get_indices_2(list1, searched1)
        expected = [3]
        self.assertEqual(result, expected)

    def test_function_2(self):
        result = get_indices_2(list2, searched2)
        expected = [0, 4, 5]
        self.assertEqual(result, expected)


class TestOfSearchFunctionThree(unittest.TestCase):

    def test_function_1(self):
        result = get_indices_3(list1, searched1)
        expected = [3]
        self.assertEqual(result, expected)

    def test_function_2(self):
        result = get_indices_3(list2, searched2)
        expected = [0, 4, 5]
        self.assertEqual(result, expected)
