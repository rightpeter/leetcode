#!/usr/bin/env python3

import unittest
from split_array_largest_sum import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.splitArray([7, 2, 5, 10, 8], 2), 18)

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.splitArray([7, 7, 7, 7, 7, 7], 3), 14)

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.splitArray([1, 2147483647], 2), 2147483647)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
