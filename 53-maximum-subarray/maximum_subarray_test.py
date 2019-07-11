#!/usr/bin/env python3

import unittest
from maximum_subarray import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.maxSubArray([1]), 1)

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.maxSubArray([-2, 1, -3, 1000, -1, 2, 3, -1, -6, -5, 1000, 4]), 1996)

    def test_4(self):
        sol = Solution()
        self.assertEqual(sol.maxSubArray([-2, -1, 3, 4, 1, 2, 1, 5, -4]), 16)

    def test_5(self):
        sol = Solution()
        self.assertEqual(sol.maxSubArray([2, 1, 3, 4, 1, 2, 1, 5, 4]), 23)

    def test_6(self):
        sol = Solution()
        self.assertEqual(sol.maxSubArray([-1]), -1)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_5()
