#!/usr/bin/env python3

import unittest
from interval_list_intersections import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(
            sol.intervalIntersection([[0, 2], [5, 10], [13, 23], [24, 25]],
                                     [[1, 5], [8, 12], [15, 24], [25, 26]]),
            [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]])

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.intervalIntersection([], [[1, 3], [4, 6]]), [])

    def test_3(self):
        sol = Solution()
        self.assertEqual(
            sol.intervalIntersection([[1, 6]], [[1, 2], [4, 6]]),
            [[1, 2], [4, 6]])


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
