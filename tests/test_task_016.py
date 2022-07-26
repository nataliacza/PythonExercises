import unittest
from challenges.task_016 import remove_repetitive

list1 = [4543, 111, 357, 5675, 2567, 8632]
expected1 = [357, 2567, 8632]

list2 = [1, 11, 123, 4525]
expected2 = [1, 123]


class TestOfRemoveRepetitiveFunctionOne(unittest.TestCase):

    def test_function_1(self):
        result = remove_repetitive(list1)
        expected = expected1
        self.assertEqual(result, expected)

    def test_function_2(self):
        result = remove_repetitive(list2)
        expected = expected2
        self.assertEqual(result, expected)
