#!/usr/bin/env python3

import unittest
from largest_rectangle_in_histogram_stack import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.largestRectangleArea([2, 1, 5, 6, 2, 3]), 10)

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.largestRectangleArea([2, 1, 2]), 3)

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.largestRectangleArea([0]), 0)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_3()
