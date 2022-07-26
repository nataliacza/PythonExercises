import unittest
from challenges.task_011 import concat, concat_2, concat_3

list1 = [[6, 2], [6, 3, 7], [3, 5]]
other1 = [[3], [4, 2], [0, 5, 1, 5]]
expected1 = [[6, 2, 3], [6, 3, 7, 4, 2], [3, 5, 0, 5, 1, 5]]

list2 = [[6, 2, 5, 2], [6, 3, 7]]
other2 = [[4, 2], [0, 5, 1, 5]]
expected2 = [[6, 2, 5, 2, 4, 2], [6, 3, 7, 0, 5, 1, 5]]

class TestOfConcatFunctionOne(unittest.TestCase):

    def test_function_1(self):
        result = concat(list1, other1)
        expected = expected1
        self.assertEqual(result, expected)

    def test_function_2(self):
        result = concat(list2, other2)
        expected = expected2
        self.assertEqual(result, expected)


class TestOfConcatFunctionTwo(unittest.TestCase):

    def test_function_1(self):
        result = concat_2(list1, other1)
        expected = expected1
        self.assertEqual(result, expected)

    def test_function_2(self):
        result = concat_2(list2, other2)
        expected = expected2
        self.assertEqual(result, expected)


class TestOfConcatFunctionThree(unittest.TestCase):

    def test_function_1(self):
        result = concat_3(list1, other1)
        expected = expected1
        self.assertEqual(result, expected)

    def test_function_2(self):
        result = concat_3(list2, other2)
        expected = expected2
        self.assertEqual(result, expected)
