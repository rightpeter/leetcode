#!/usr/bin/env python3

import unittest
from rectangle_area_ii import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(
            sol.rectangleArea([[0, 0, 2, 2], [1, 0, 2, 3], [1, 0, 3, 1]]), 6)

    def test_2(self):
        sol = Solution()
        self.assertEqual(
            sol.rectangleArea([[0, 0, 1000000000, 1000000000]]), 49)

    def test_3(self):
        sol = Solution()
        self.assertEqual(
            sol.rectangleArea([[1, 0, 2, 2], [3, 1, 4, 3]]), 4)


if __name__ == '__main__':
    # unittest.main()
    TestSolution().test_3()
