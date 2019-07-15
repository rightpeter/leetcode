#!/usr/bin/env python3

import unittest
from unique_paths import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.uniquePaths(3, 2), 3)

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.uniquePaths(7, 3), 28)

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.uniquePaths(10, 10), 48620)

    def test_4(self):
        sol = Solution()
        self.assertEqual(sol.uniquePaths(0, 10), 0)

    def test_5(self):
        sol = Solution()
        self.assertEqual(sol.uniquePaths(10, 0), 0)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
