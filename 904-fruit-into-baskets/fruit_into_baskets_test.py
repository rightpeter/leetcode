#!/usr/bin/env python3

import unittest
from fruit_into_baskets import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.totalFruit([1, 2, 1]), 3)

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.totalFruit([0, 1, 2, 2]), 3)

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.totalFruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]), 5)

    def test_4(self):
        sol = Solution()
        self.assertEqual(sol.totalFruit([]), 0)

    def test_5(self):
        sol = Solution()
        self.assertEqual(sol.totalFruit([1]), 1)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
