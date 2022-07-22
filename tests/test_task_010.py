import unittest
from challenges.task_010 import convert

list1 = [
    {"user": "joe", "technology": "python"},
    {"user": "tom", "technology": "c"},
    {"user": "michael", "technology": "cloud"},
    {"user": "bob", "technology": "php"},
    {"user": "lil", "technology": "html"},
    {"user": "alice", "technology": "sql"}
]
expected1 = {
    "user": ["joe", "tom", "michael", "bob", "lil", "alice"],
    "technology": ["python", "c", "cloud", "php", "html", "sql"]
}

class TestOfDictConvertFunctionOne(unittest.TestCase):

    def test_function_1(self):
        result = convert(list1)
        expected = expected1
        self.assertEqual(result, expected)
