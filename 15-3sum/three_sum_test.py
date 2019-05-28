#!/usr/bin/env python3

import unittest
from three_sum import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(
            sol.threeSum([-1, 0, 1, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]])

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.threeSum([]), [])

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.threeSum([-1, -2]), [])

    def test_4(self):
        sol = Solution()
        self.assertEqual(sol.threeSum([0, 0, 0]), [[0, 0, 0]])

    def test_5(self):
        sol = Solution()
        self.assertEqual(sol.threeSum([-1, -1, 0, 1, 1]), [[-1, 0, 1]])

    def test_6(self):
        sol = Solution()
        self.assertEqual(sol.threeSum([0, 0, 0, 0, 0]), [[0, 0, 0]])

    def test_7(self):
        sol = Solution()
        self.assertEqual(sol.threeSum([-1, 0, 1]), [[-1, 0, 1]])

    def test_8(self):
        sol = Solution()
        self.assertEqual(sol.threeSum([1, 2, -2, -1]), [])


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_6()
