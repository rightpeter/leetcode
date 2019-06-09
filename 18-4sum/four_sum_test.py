#!/usr/bin/env python3

import unittest
from four_sum import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(
            sol.fourSum([1, 0, -1, 0, -2, 2], 0),
            [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]])

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.fourSum([1, 0], 0), [])

    def test_3(self):
        sol = Solution()
        self.assertEqual(
            sol.fourSum([-3, -2, -1, 0, 0, 1, 2, 3], 0),
            [[-3, -2, 2, 3], [-3, -1, 1, 3], [-3, 0, 0, 3], [-3, 0, 1, 2],
             [-2, -1, 0, 3], [-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]])

    def test_4(self):
        sol = Solution()
        self.assertEqual(
            sol.fourSum([-1, 0, -5, -2, -2, -4, 0, 1, -2],
                        -9), [[-5, -4, -1, 1], [-5, -4, 0, 0], [-5, -2, -2, 0],
                              [-4, -2, -2, -1]])


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_3()
