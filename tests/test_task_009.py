import unittest
from challenges.task_009 import get_indices

list1 = ["www.google.com", "http", 200, 1.25, False, "text"]
# [0, 1, 5]

list2 = []
# []

list3 = [1, 2, 3, 4]
# []

class TestOfIndexFunctionOne(unittest.TestCase):

    def test_function_1(self):
        result = get_indices(list1)
        expected = [0, 1, 5]
        self.assertEqual(result, expected)

    def test_function_2(self):
        result = get_indices(list2)
        expected = []
        self.assertEqual(result, expected)

    def test_function_3(self):
        result = get_indices(list3)
        expected = []
        self.assertEqual(result, expected)
