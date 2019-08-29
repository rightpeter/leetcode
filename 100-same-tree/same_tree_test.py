#!/usr/bin/env python3

import unittest
from same_tree import Solution
from tree_helper import TreeHelper


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        input_tree1 = [1, 2, 3]
        t1 = TreeHelper.list_to_tree(input_tree1)
        input_tree2 = [1, 2, 3]
        t2 = TreeHelper.list_to_tree(input_tree2)

        self.assertEqual(sol.isSameTree(t1, t2), True)

    def test_2(self):
        sol = Solution()
        input_tree1 = [1, 2]
        t1 = TreeHelper.list_to_tree(input_tree1)
        input_tree2 = [1, None, 2]
        t2 = TreeHelper.list_to_tree(input_tree2)

        self.assertEqual(sol.isSameTree(t1, t2), False)

    def test_3(self):
        sol = Solution()
        input_tree1 = []
        t1 = TreeHelper.list_to_tree(input_tree1)
        input_tree2 = [1, None, 2]
        t2 = TreeHelper.list_to_tree(input_tree2)

        self.assertEqual(sol.isSameTree(t1, t2), False)

    def test_4(self):
        sol = Solution()
        input_tree1 = [1, None, 2]
        t1 = TreeHelper.list_to_tree(input_tree1)
        input_tree2 = []
        t2 = TreeHelper.list_to_tree(input_tree2)

        self.assertEqual(sol.isSameTree(t1, t2), False)

    def test_5(self):
        sol = Solution()
        input_tree1 = []
        t1 = TreeHelper.list_to_tree(input_tree1)
        input_tree2 = []
        t2 = TreeHelper.list_to_tree(input_tree2)

        self.assertEqual(sol.isSameTree(t1, t2), True)

    def test_6(self):
        sol = Solution()
        input_tree1 = [2, None, 4]
        t1 = TreeHelper.list_to_tree(input_tree1)
        input_tree2 = [2, 3, 4]
        t2 = TreeHelper.list_to_tree(input_tree2)

        self.assertEqual(sol.isSameTree(t1, t2), False)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_6()
