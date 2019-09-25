#!/usr/bin/env python3

import unittest
from flip_equivalent_binary_trees import Solution
from bin_tree_helper import TreeHelper


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        input_list1 = [1, 2, 3, 4, 5, 6, None, None, None, 7, 8]
        input_tree1 = TreeHelper.list_to_tree(input_list1)
        input_list2 = [1, 3, 2, None, 6, 4, 5, None, None, None, None, 8, 7]
        input_tree2 = TreeHelper.list_to_tree(input_list2)

        self.assertEqual(sol.flipEquiv(input_tree1, input_tree2), True)

    def test_2(self):
        sol = Solution()
        input_list1 = [1, 2, 3, 4, 5, 6, None, None, None, 7, 8]
        input_tree1 = TreeHelper.list_to_tree(input_list1)
        input_list2 = [1, 3, 2, None, 6, 10, 5, None, None, None, None, 8, 7]
        input_tree2 = TreeHelper.list_to_tree(input_list2)

        self.assertEqual(sol.flipEquiv(input_tree1, input_tree2), False)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
