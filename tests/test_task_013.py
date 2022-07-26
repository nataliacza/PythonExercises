import unittest
from challenges.task_013 import sort_by_row

list1 = [[4, 7, 2, 7, 9, 1], [6, 3, 2, 8, 8], [9, 7, 3, 2, 7]]
expected1 = [[1, 2, 4, 7, 7, 9], [2, 3, 6, 8, 8], [2, 3, 7, 7, 9]]

list2 = [[5, -2, 3, 7, 4], [6, 3]]
expected2 = [[-2, 3, 4, 5, 7], [3, 6]]

class TestOfSortFunctionOne(unittest.TestCase):

    def test_function_1(self):
        result = sort_by_row(list1)
        expected = expected1
        self.assertEqual(result, expected)

    def test_function_2(self):
        result = sort_by_row(list2)
        expected = expected2
        self.assertEqual(result, expected)
