"""
    Unittest for max_integer
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInt(unittest.TestCase):
    """Test max_int"""

    def test_empty_list(self):
        """"tests an empty list"""
        list = []
        res = max_integer(list)
        self.assertIsNone(res)

    def test_no_arg(self):
        """tests when no argument are passed to max_int"""
        res = max_integer()
        self.assertIsNone(res)

    def test_max_of_len_one(self):
        """tests list of one argument"""
        list = [9]
        res = max_integer(list)
        self.assertEqual(res, 9)

    def test_max_negative_int(self):
        """tests only negative integer in list""""
        list = [-1, -3, -5, -8]
        res = max_integer(list)
        self.assertEqual(res, -1)

    def test_max_is_8(self):
        """tests list of mixed integers positive/negative"""
        list = [1, 8, 0, -3]
        res = max_integer(list)
        self.assertEqual(res, 8)
