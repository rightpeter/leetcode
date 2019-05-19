#!/usr/bin/env python3

import unittest
from the_skyline_problem import Solution


class TestSkyLine(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(
            sol.getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10],
                            [19, 24, 8]]),
            [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]])

    def test_2(self):
        sol = Solution()
        self.assertEqual(
            sol.getSkyline([[2, 9, 10], [9, 12, 15]]),
            [[2, 10], [9, 15], [12, 0]])

    def test_3(self):
        sol = Solution()
        self.assertEqual(
            sol.getSkyline([[1, 2, 1], [1, 2, 2], [1, 2, 3]]), [[1, 3], [2, 0]])


if __name__ == '__main__':
    unittest.main()
