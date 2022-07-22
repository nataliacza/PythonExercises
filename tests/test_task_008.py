import unittest
from challenges.task_008 import get_indicates

list1 = [4, 3, 5, 2]
searched1 = 2
# [3]

list2 = ["Q", "DQ", "DQ", "DQ", "Q", "Q"]
searched2 = "Q"
# [0, 4, 5]

class TestOfSearchFunctionOne(unittest.TestCase):

    def test_function_1(self):
        result = get_indicates(list1, searched1)
        expected = [3]
        self.assertEqual(result, expected)

    def test_function_2(self):
        result = get_indicates(list2, searched2)
        expected = [0, 4, 5]
        self.assertEqual(result, expected)
