#!/usr/bin/env python3

import unittest
from the_maze_ii import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(
            sol.shortestDistance(
                [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0],
                 [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]], [0, 4], [4, 4]), 12)

    def test_2(self):
        sol = Solution()
        self.assertEqual(
            sol.shortestDistance(
                [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0],
                 [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]], [0, 4], [3, 2]), -1)

    def test_3(self):
        sol = Solution()
        self.assertEqual(
            sol.shortestDistance(
                [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0],
                 [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]], [0, 4], [3, 2]), -1)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
