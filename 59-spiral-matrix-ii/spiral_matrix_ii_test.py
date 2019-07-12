#!/usr/bin/env python3

import unittest
from spiral_matrix_ii import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.generateMatrix(3), [[1, 2, 3], [8, 9, 4], [7, 6, 5]])

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.generateMatrix(4), [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]])

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.generateMatrix(1), [[1]])


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
