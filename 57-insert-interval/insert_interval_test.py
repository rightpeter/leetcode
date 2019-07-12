#!/usr/bin/env python3

import unittest
from insert_interval import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.insert([[1, 3], [6, 9]], [2, 5]), [[1, 5], [6, 9]])

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]), [[1, 2], [3, 10], [12, 16]])

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.insert([], [4, 8]), [[4, 8]])

    def test_4(self):
        sol = Solution()
        self.assertEqual(sol.insert([[1, 10]], [4, 8]), [[1, 10]])


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
