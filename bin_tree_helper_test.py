#!/usr/bin/env python3

import unittest
from bin_tree_helper import TreeNode, TreeHelper


class TestHelper(unittest.TestCase):

    def test_tree_to_list(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)

        self.assertEqual(TreeHelper.tree_to_list(root), [1, None, 2, 3])

    def test_list_to_tree_and_reverse(self):
        test_list = [1, None, 2, 3]
        tmp_tree = TreeHelper.list_to_tree(test_list)
        self.assertEqual(TreeHelper.tree_to_list(tmp_tree), test_list)

        test_list = [1, None, 2, None, 3]
        tmp_tree = TreeHelper.list_to_tree(test_list)
        self.assertEqual(TreeHelper.tree_to_list(tmp_tree), test_list)

        test_list = []
        tmp_tree = TreeHelper.list_to_tree(test_list)
        self.assertEqual(TreeHelper.tree_to_list(tmp_tree), test_list)

        test_list = [1, 2, None, None, 3]
        tmp_tree = TreeHelper.list_to_tree(test_list)
        self.assertEqual(TreeHelper.tree_to_list(tmp_tree), test_list)

        test_list = [1, 3, 6, None, None, None, 2, 3, 7, 4, None, 2, None, 3]
        tmp_tree = TreeHelper.list_to_tree(test_list)
        self.assertEqual(TreeHelper.tree_to_list(tmp_tree), test_list)

    def test_print_tree(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)

        self.assertEqual(
            TreeHelper.print_tree(root),
            '1\nNone\t2\t\nNone\tNone\t3\tNone\t\n')

    def test_inorder_traversal(self):
        test_list = [1, None, 2, 3]
        tmp_tree = TreeHelper.list_to_tree(test_list)
        self.assertEqual(TreeHelper.inorder_traversal(tmp_tree), [1, 3, 2])


if __name__ == '__main__':
    unittest.main()
    # TestHelper().test_inorder_traversal()
