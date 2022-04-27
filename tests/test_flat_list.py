# test_flat_list.py
import unittest
from . import tc

class TestFlatList(unittest.TestCase):
    
    def setUp(self):
        self.flatlist = tc.FlatList()
        self.list_int = [1, [2, [3, [4, 5]], 6, [7], [8, 9, 10]], 11]
        self.empty_list = []
        self.list_multiple_type = ["a",[1, 2, [-1, None, [1, 2, 3, ["a", "b", "c"]]], 999],"z",]
        self.false_list_string = "A"
        self.false_list_int = 1
        self.false_list_none = None

    def tearDown(self):
        # Add teardown code here!
        del self.flatlist

    def test_flat_valid_list(self):
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        self.flatlist.list = self.list_int
        result = self.flatlist.list
        self.assertEqual(expected, result)

    def test_flat_nested_empty_list(self):
        expected = []
        self.flatlist.list = self.empty_list
        result = self.flatlist.list
        self.assertEqual(expected, result)

    def test_flat_nested_multi_type_list(self):
        expected = ["a", 1, 2, -1, None, 1, 2, 3, "a", "b", "c", 999, "z"]
        self.flatlist.list = self.list_multiple_type
        result = self.flatlist.list
        self.assertEqual(expected, result)
    
    #@unittest.skip 
    def test_raise_exception_when_passing_string(self):
        with self.assertRaises(Exception) as context:
            self.flatlist.list = self.false_list_string
        self.assertTrue(isinstance(context.exception, TypeError))
        self.assertEqual("Input should be a list.", str(context.exception))
    
    def test_raise_exception_when_passing_int(self):
        with self.assertRaises(Exception) as context:
            self.flatlist.list = self.false_list_int
        self.assertTrue(isinstance(context.exception, TypeError))
        self.assertEqual("Input should be a list.", str(context.exception))
    
    def test_raise_exception_when_none(self):
        with self.assertRaises(Exception) as context:
            self.flatlist.list = self.false_list_none
        self.assertTrue(isinstance(context.exception, Exception))
        self.assertEqual("Input should not be null.", str(context.exception))


if __name__ == "__main__":
    unittest.main()
