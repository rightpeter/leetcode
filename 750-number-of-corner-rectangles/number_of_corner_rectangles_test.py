#!/usr/bin/env python3

import unittest
from number_of_corner_rectangles import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(
            sol.countCornerRectangles([[1, 0, 0, 1, 0], [0, 0, 1, 0, 1],
                                       [0, 0, 0, 1, 0], [1, 0, 1, 0, 1]]), 1)

    def test_2(self):
        sol = Solution()
        self.assertEqual(
            sol.countCornerRectangles([[1, 1, 1], [1, 1, 1], [1, 1, 1]]), 9)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
