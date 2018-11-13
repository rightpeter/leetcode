import unittest
from serialize_and_deserialize_binary_tree import Codec
from serialize_and_deserialize_binary_tree import TreeNode


class TestBinaryTree(unittest.TestCase):

    def test_1(self):
        codec = Codec()
        tree_str = "[1,2,3,null,null,4,5]"
        self.assertEqual(codec.serialize(codec.deserialize(tree_str)), tree_str)

    def test_2(self):
        codec = Codec()
        tree_str = '[]'
        self.assertEqual(codec.serialize(codec.deserialize(tree_str)), tree_str)

    def test_3(self):
        codec = Codec()
        tree_str = '[5,4,7,3,null,2,null,-1,null,null,null,9]'
        self.assertEqual(codec.serialize(codec.deserialize(tree_str)), tree_str)

    def test_4(self):
        codec = Codec()
        self.assertEqual(codec.serialize(None), '[]')

    def test_5(self):
        codec = Codec()
        self.assertEqual(codec.deserialize('[]'), None)

    def test_6(self):
        codec = Codec()
        node = TreeNode(3)
        self.assertEqual(codec.serialize(node), '[3]')

    def test_7(self):
        codec = Codec()
        self.assertEqual(codec.deserialize(codec.serialize(None)), None)


if __name__ == '__main__':
    unittest.main()
    # TestBinaryTree().test_5()
