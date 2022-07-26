import unittest
from challenges.task_012 import concat

list1 = [[6, 2], [6, 3, 7], [3, 5]]
other1 = [[3], [4, 2], [0, 5, 1, 5]]
expected1 = [[6, 2, 3], [6, 3, 7, 4, 2], [3, 5, 0, 5, 1, 5]]

list2 = [[6, 2, 5, 2], [6, 3, 7]]
other2 = [[4, 2], [0, 5, 1, 5], [4]]
expected2 = ValueError

class TestOfConcatWithValidationFunctionOne(unittest.TestCase):

    def test_function_1(self):
        result = concat(list1, other1)
        expected = expected1
        self.assertEqual(result, expected)

    def test_function_2(self):
        with self.assertRaises(ValueError):
            concat(list2, other2)
