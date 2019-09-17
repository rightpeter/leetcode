#!/usr/bin/env python3

import unittest
from binary_tree_maximum_path_sum import Solution
from bin_tree_helper import TreeHelper


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        input_list = [1, 2, 3]
        self.assertEqual(sol.maxPathSum(TreeHelper.list_to_tree(input_list)), 6)

    def test_2(self):
        sol = Solution()
        input_list = [-10, 9, 20, None, None, 15, 7]
        self.assertEqual(
            sol.maxPathSum(TreeHelper.list_to_tree(input_list)), 42)

    def test_3(self):
        sol = Solution()
        input_list = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
        self.assertEqual(
            sol.maxPathSum(TreeHelper.list_to_tree(input_list)), 48)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_2()
