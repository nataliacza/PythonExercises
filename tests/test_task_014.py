import unittest
from challenges.task_014 import top3, top3_2

list1 = [[4, 7, 2, 7, 9, 1, 3], [6, 3, 2, 8, 8, 7], [9, 7, 3, 2, 10, 2]]
expected1 = [[9, 7, 7], [8, 8, 7], [10, 9, 7]]


class TestOfTop3FunctionOne(unittest.TestCase):

    def test_function_1(self):
        result = top3(list1)
        expected = expected1
        self.assertEqual(result, expected)


class TestOfTop3FunctionTwo(unittest.TestCase):

    def test_function_1(self):
        result = top3_2(list1)
        expected = expected1
        self.assertEqual(result, expected)
