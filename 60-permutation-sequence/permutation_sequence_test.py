#!/usr/bin/env python3

import unittest
from permutation_sequence import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.getPermutation(3, 3), "213")

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.getPermutation(4, 9), "2314")

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.getPermutation(1, 1), "1")

    def test_4(self):
        sol = Solution()
        self.assertEqual(sol.getPermutation(2, 1), "12")

    def test_5(self):
        sol = Solution()
        self.assertEqual(sol.getPermutation(2, 2), "21")

    def test_6(self):
        sol = Solution()
        self.assertEqual(sol.getPermutation(3, 1), "123")

    def test_7(self):
        sol = Solution()
        self.assertEqual(sol.getPermutation(3, 2), "132")


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_7()
