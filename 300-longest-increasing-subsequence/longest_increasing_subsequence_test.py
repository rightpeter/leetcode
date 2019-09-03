#!/usr/bin/env python3

import unittest
from longest_increasing_subsequence_nlogn import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]), 4)

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.lengthOfLIS([0]), 1)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
