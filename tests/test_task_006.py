import unittest
from challenges.task_006 import reverse_words

text1 = "python is the best"  # "best the is python"
text2 = "you should learn python"  # "python learn should you"


class TestOfSwapFunctionOne(unittest.TestCase):

    def test_function_1(self):
        result = reverse_words(text1)
        expected = "best the is python"
        self.assertEqual(result, expected)

    def test_function_2(self):
        result = reverse_words(text2)
        expected = "python learn should you"
        self.assertEqual(result, expected)
