import unittest
from challenges.task_007 import remove_common_elements

list1 = [4, 3, 5, 2]
list2 = [3, 8]
# [4, 5, 2], [8]

listA = [4, 3, 5, 2]
listB = [1, 8]
# [4, 3, 5, 2], [1, 8]

listX = [4, 2, 4]
listY = [2, 8]
# [4, 4], [8]

class TestOfSwapFunctionOne(unittest.TestCase):

    def test_function_1(self):
        result = remove_common_elements(list1, list2)
        expected = ([4, 5, 2], [8])
        self.assertEqual(result, expected)

    def test_function_2(self):
        result = remove_common_elements(listA, listB)
        expected = ([4, 3, 5, 2], [1, 8])
        self.assertEqual(result, expected)

    def test_function_3(self):
        result = remove_common_elements(listX, listY)
        expected = ([4, 4], [8])
        self.assertEqual(result, expected)
