import unittest
from serialize_and_deserialize_binary_tree import Codec

class TestBinaryTree(unittest.TestCase):
    def test_1(self):
        codec = Codec()
        tree_str = '[[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]'
        self.assertEqual(codec.serialize(codec.deserialize(tree_str)), tree_str)

    def test_2(self):
        codec = Codec()
        tree_str = '[]'
        self.assertEqual(codec.serialize(codec.deserialize(tree_str)), tree_str)

    def test_3(self):
        codec = Codec()
        tree_str = '[[0, 5], [1, 4], [2, 7], [3, 3], [5, 2], [7, -1], [11, 9]]'
        self.assertEqual(codec.serialize(codec.deserialize(tree_str)), tree_str)

if __name__ == '__main__':
    unittest.main()