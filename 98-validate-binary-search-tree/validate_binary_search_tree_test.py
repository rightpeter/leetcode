#!/usr/bin/env python3

import unittest
from validate_binary_search_tree import Solution
from bin_tree_helper import TreeHelper


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        input_list = [2, 1, 3]
        input_tree = TreeHelper.list_to_tree(input_list)
        self.assertEqual(sol.isValidBST(input_tree), True)

    def test_2(self):
        sol = Solution()
        input_list = [5, 1, 4, None, None, 3, 6]
        input_tree = TreeHelper.list_to_tree(input_list)
        self.assertEqual(sol.isValidBST(input_tree), False)

    def test_3(self):
        sol = Solution()
        input_list = [3, 1, 5, None, None, 4, 6]
        input_tree = TreeHelper.list_to_tree(input_list)
        self.assertEqual(sol.isValidBST(input_tree), True)

    def test_4(self):
        sol = Solution()
        input_list = [1, 1]
        input_tree = TreeHelper.list_to_tree(input_list)
        self.assertEqual(sol.isValidBST(input_tree), False)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
