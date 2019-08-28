#!/usr/bin/env python3

import unittest
from binary_tree_inorder_traversal import Solution
from tree_helper import TreeHelper


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        test_list = [1, None, 2, 3]
        tmp_tree = TreeHelper.list_to_tree(test_list)
        self.assertEqual(sol.inorderTraversal(tmp_tree), [1, 3, 2])

    def test_2(self):
        sol = Solution()
        test_list = [1, None, 2, None, 3]
        tmp_tree = TreeHelper.list_to_tree(test_list)
        self.assertEqual(sol.inorderTraversal(tmp_tree), [1, 2, 3])

    def test_3(self):
        sol = Solution()
        test_list = [1, 3, 6, None, None, None, 2, 3, 7, 4, None, 2, None, 3]
        tmp_tree = TreeHelper.list_to_tree(test_list)
        self.assertEqual(
            sol.inorderTraversal(tmp_tree), [3, 1, 6, 3, 4, 3, 2, 2, 7])

    def test_4(self):
        sol = Solution()
        test_list = []
        tmp_tree = TreeHelper.list_to_tree(test_list)
        self.assertEqual(sol.inorderTraversal(tmp_tree), [])

    def test_5(self):
        sol = Solution()
        test_list = [1, 2, None, 3, None, 4, None, 5]
        tmp_tree = TreeHelper.list_to_tree(test_list)
        self.assertEqual(sol.inorderTraversal(tmp_tree), [5, 4, 3, 2, 1])

    def test_6(self):
        sol = Solution()
        test_list = [1, None, 2, None, 3, None, 4, None, 5]
        tmp_tree = TreeHelper.list_to_tree(test_list)
        self.assertEqual(sol.inorderTraversal(tmp_tree), [1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_2()
