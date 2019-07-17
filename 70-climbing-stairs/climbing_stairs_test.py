#!/usr/bin/env python3

import unittest
from climbing_stairs import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.climbStairs(2), 2)

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.climbStairs(3), 3)

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.climbStairs(1), 1)

    def test_4(self):
        sol = Solution()
        self.assertEqual(sol.climbStairs(7), 21)

    def test_5(self):
        sol = Solution()
        self.assertEqual(sol.climbStairs(8), 34)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_5()
