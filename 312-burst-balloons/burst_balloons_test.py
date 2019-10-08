#!/usr/bin/env python3

import unittest
from burst_balloons import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.maxCoins([3, 1, 5, 8]), 167)

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.maxCoins([]), 0)

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.maxCoins([3]), 3)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
