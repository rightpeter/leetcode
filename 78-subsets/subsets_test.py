#!/usr/bin/env python3

import unittest
from subsets import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.subsets([1, 2, 3]), [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]])

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.subsets([1]), [[], [1]])

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.subsets([]), [[]])


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
