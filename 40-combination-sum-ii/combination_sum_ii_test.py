#!/usr/bin/env python3

import unittest
from combination_sum_ii_tmp import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8), [[2, 6], [1, 7], [1, 2, 5], [1, 1, 6]])

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.combinationSum2([2, 5, 2, 1, 2], 5), [[5], [1, 2, 2]])

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.combinationSum2([2], 5), [])

    def test_4(self):
        sol = Solution()
        self.assertEqual(sol.combinationSum2([2, 3, 5, 7], 30), [])

    def test_5(self):
        sol = Solution()
        self.assertEqual(sol.combinationSum2([2, 3, 5, 7], 17), [[2, 3, 5, 7]])


if __name__ == '__main__':
    # unittest.main()
    TestSolution().test_1()
