#!/usr/bin/env python3

import unittest
from split_array_into_consecutive_subsequences import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.isPossible([1, 2, 3, 3, 4, 5]), True)

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.isPossible([1, 2, 3, 3, 4, 4, 5, 5]), True)

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.isPossible([1, 2, 3, 4, 5, 6, 7, 8, 9]), True)

    def test_4(self):
        sol = Solution()
        self.assertEqual(sol.isPossible([1, 2, 3, 3, 3, 3, 7, 8, 9]), False)

    def test_5(self):
        sol = Solution()
        self.assertEqual(sol.isPossible([1, 2, 3, 4, 6, 7, 8, 9]), True)

    def test_6(self):
        sol = Solution()
        self.assertEqual(sol.isPossible([1, 2, 3, 4, 4, 5]), False)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_6()
