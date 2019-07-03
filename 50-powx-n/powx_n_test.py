#!/usr/bin/env python3

import unittest
from powx_n import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        self.assertAlmostEqual(sol.myPow(2.00000, 10), 1024.00000)

    def test_2(self):
        sol = Solution()
        self.assertAlmostEqual(sol.myPow(2.10000, 3), 9.26100)

    def test_3(self):
        sol = Solution()
        self.assertAlmostEqual(sol.myPow(2.00000, -2), 0.25000)

    def test_4(self):
        sol = Solution()
        self.assertAlmostEqual(sol.myPow(2.00000, 0), 1.00000)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
