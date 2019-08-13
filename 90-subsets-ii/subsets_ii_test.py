#!/usr/bin/env python3

import unittest
from subsets_ii import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(
            sol.subsetsWithDup([1, 2, 2]),
            [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]])

    def test_2(self):
        sol = Solution()
        self.assertEqual(
            sol.subsetsWithDup([1, 2, 3]),
            [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]])

    def test_3(self):
        sol = Solution()
        self.assertEqual(
            sol.subsetsWithDup([1, 1, 1]),
            [[], [1], [1, 1], [1, 1, 1]])


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
