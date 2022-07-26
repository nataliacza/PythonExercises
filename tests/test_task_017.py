import unittest
from challenges.task_017 import calculate

list1 = [2, 6, 2, 8, 1, 3, 10, 3]
expected1 = [8, 10]

list2 = [1, 6, 5, 2, 8, 11, 3, 10, 3]
k2 = 3
expected2 = [2, 8, 11, 3, 10]


class TestOfCalculateFunctionOne(unittest.TestCase):

    def test_function_1(self):
        result = calculate(list1)
        expected = expected1
        self.assertEqual(result, expected)

    def test_function_2(self):
        result = calculate(list2, k2)
        expected = expected2
        self.assertEqual(result, expected)
