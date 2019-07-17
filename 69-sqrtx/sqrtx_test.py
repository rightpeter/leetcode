#!/usr/bin/env python3

import unittest
from sqrtx import Solution
from math import sqrt


class TestSolution(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        for x in range(1000):
            self.assertEqual(sol.mySqrt(x), int(sqrt(x)))


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
