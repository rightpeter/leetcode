#!/usr/bin/env python3

import unittest
from divide_two_integers import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.divide(10, 3), 3)

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.divide(7, -3), -2)

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.divide(8, 2), 4)

    def test_4(self):
        sol = Solution()
        self.assertEqual(sol.divide(-2147483648, -1), 2147483647)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
