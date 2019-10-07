#!/usr/bin/env python3

import unittest
from house_robber import Solution
from bin_tree_helper import TreeHelper


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        input_list = [3, 2, 3, None, 3, None, 1]
        input_tree = TreeHelper.list_to_tree(input_list)
        self.assertEqual(sol.rob(input_tree), 7)

    def test_2(self):
        sol = Solution()
        input_list = [3, 4, 5, 1, 3, None, 1]
        input_tree = TreeHelper.list_to_tree(input_list)
        self.assertEqual(sol.rob(input_tree), 9)

    def test_3(self):
        sol = Solution()
        input_list = []
        input_tree = TreeHelper.list_to_tree(input_list)
        self.assertEqual(sol.rob(input_tree), 0)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
