#!/usr/bin/env python3

import unittest
from n_queens_ii import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.totalNQueens(4), 2)

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.totalNQueens(5), 10)

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.totalNQueens(1), 1)

    def test_4(self):
        sol = Solution()
        self.assertEqual(sol.totalNQueens(0), 0)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_2()
