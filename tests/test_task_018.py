import unittest
from challenges.task_018 import calculate

sequence1 = "python is the"
expected1 = [
    "python is the",
    "python the is",
    "is the python",
    "is python the",
    "the is python",
    "the python is"
]
# 3! == 6

sequence2 = "python is the best"
expected2 = [
    "python is the best",
    "python is best the",
    "python the is best",
    "python the best is",
    "python best is the",
    "python best the is",
    "is the best python",
    "is the python best",
    "is best python the",
    "is best the python",
    "is python the best",
    "is python best the",
    "the best python is",
    "the best is python",
    "the is best python",
    "the is python best",
    "the python is best",
    "the python best is",
    "best python is the",
    "best python the is",
    "best is python the",
    "best is the python",
    "best python is the",
    "best python the is"
]
# 4! == 24

class TestOfPermutationFunctionOne(unittest.TestCase):

    def test_function_1(self):
        result = calculate(sequence1)
        expected = expected1
        self.assertEqual(result.sort(), expected.sort())

    def test_function_2(self):
        result = calculate(sequence2)
        expected = expected2
        self.assertEqual(result.sort(), expected.sort())
