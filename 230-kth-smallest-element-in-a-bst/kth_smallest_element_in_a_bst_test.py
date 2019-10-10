#!/usr/bin/env python3

import unittest
from kth_smallest_element_in_a_bst import Solution
from bin_tree_helper import TreeHelper


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        input_list = [3, 1, 4, None, 2]
        input_tree = TreeHelper.list_to_tree(input_list)
        self.assertEqual(sol.kthSmallest(input_tree, 1), 1)

    def test_2(self):
        sol = Solution()
        input_list = [5, 3, 6, 2, 4, None, None, 1]
        input_tree = TreeHelper.list_to_tree(input_list)
        self.assertEqual(sol.kthSmallest(input_tree, 3), 3)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
