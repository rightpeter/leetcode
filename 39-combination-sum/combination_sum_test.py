#!/usr/bin/env python3

import unittest
from combination_sum_dfs import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.combinationSum([2, 3, 6, 7], 7), [[2, 2, 3], [7]])

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.combinationSum([2, 3, 5], 8), [[2, 2, 2, 2], [2, 3, 3], [3, 5]])

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.combinationSum([3, 5], 4), [])

    def test_4(self):
        sol = Solution()
        self.assertEqual(sol.combinationSum([3], 9), [[3, 3, 3]])

    def test_5(self):
        sol = Solution()
        self.assertEqual(sol.combinationSum([], 9), [])


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_2()
