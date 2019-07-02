#!/usr/bin/env python3

import unittest
from first_missing_positive import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.firstMissingPositive([1, 2, 0]), 3)

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.firstMissingPositive([3, 4, -1, 1]), 2)

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.firstMissingPositive([7, 8, 9, 11, 12]), 1)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
