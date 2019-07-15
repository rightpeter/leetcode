#!/usr/bin/env python3

import unittest
from unique_paths_ii import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]), 2)

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.uniquePathsWithObstacles([[1, 0]]), 0)

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.uniquePathsWithObstacles([[0, 1]]), 0)

    def test_4(self):
        sol = Solution()
        self.assertEqual(sol.uniquePathsWithObstacles([[0], [1]]), 0)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
