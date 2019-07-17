#!/usr/bin/env python3

import unittest
from plus_one import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.plusOne([1, 2, 3]), [1, 2, 4])

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.plusOne([4, 3, 2, 1]), [4, 3, 2, 2])

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.plusOne([4, 3, 2, 9]), [4, 3, 3, 0])

    def test_4(self):
        sol = Solution()
        self.assertEqual(sol.plusOne([0]), [1])

    def test_5(self):
        sol = Solution()
        self.assertEqual(sol.plusOne([]), [])

    def test_6(self):
        sol = Solution()
        self.assertEqual(sol.plusOne([9]), [1, 0])

    def test_7(self):
        sol = Solution()
        self.assertEqual(sol.plusOne([9, 9]), [1, 0, 0])


if __name__ == '__main__':
    # unittest.main()
    TestSolution().test_7()
