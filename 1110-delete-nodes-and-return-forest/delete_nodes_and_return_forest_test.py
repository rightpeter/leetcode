#!/usr/bin/env python3

import unittest
from delete_nodes_and_return_forest import Solution
from bin_tree_helper import TreeHelper


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        input_list = [1, 2, 3, 4, 5, 6, 7]
        input_tree = TreeHelper.list_to_tree(input_list)
        res = sol.delNodes(input_tree, [3, 5])
        res = [TreeHelper.tree_to_list(root) for root in res]
        self.assertEqual(res, [[1, 2, None, 4], [6], [7]])

    def test_2(self):
        sol = Solution()
        input_list = [1, 2, None, 4, 3]
        input_tree = TreeHelper.list_to_tree(input_list)
        res = sol.delNodes(input_tree, [2, 3])
        res = [TreeHelper.tree_to_list(root) for root in res]
        self.assertEqual(res, [[1], [4]])


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_2()
