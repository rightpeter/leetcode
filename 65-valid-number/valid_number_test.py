#!/usr/bin/env python3

import unittest
from valid_number import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.isNumber('0'), True)

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.isNumber(' 0.1 '), True)

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.isNumber('abc'), False)

    def test_4(self):
        sol = Solution()
        self.assertEqual(sol.isNumber('1 a'), False)

    def test_5(self):
        sol = Solution()
        self.assertEqual(sol.isNumber('2e10'), True)

    def test_6(self):
        sol = Solution()
        self.assertEqual(sol.isNumber(' -90e3'), True)

    def test_7(self):
        sol = Solution()
        self.assertEqual(sol.isNumber(' 1e'), False)

    def test_8(self):
        sol = Solution()
        self.assertEqual(sol.isNumber('e3'), False)

    def test_9(self):
        sol = Solution()
        self.assertEqual(sol.isNumber(' 6e-1'), True)

    def test_10(self):
        sol = Solution()
        self.assertEqual(sol.isNumber(' 99e2.5'), False)

    def test_11(self):
        sol = Solution()
        self.assertEqual(sol.isNumber('53.5e93'), True)

    def test_12(self):
        sol = Solution()
        self.assertEqual(sol.isNumber(' --6 '), False)

    def test_13(self):
        sol = Solution()
        self.assertEqual(sol.isNumber('-+3'), False)

    def test_14(self):
        sol = Solution()
        self.assertEqual(sol.isNumber('95a54e53'), False)

    def test_15(self):
        sol = Solution()
        self.assertEqual(sol.isNumber(''), False)

    def test_16(self):
        sol = Solution()
        self.assertEqual(sol.isNumber('      '), False)

    def test_17(self):
        sol = Solution()
        self.assertEqual(sol.isNumber('.1'), True)

    def test_18(self):
        sol = Solution()
        self.assertEqual(sol.isNumber('.'), False)

    def test_19(self):
        sol = Solution()
        self.assertEqual(sol.isNumber('01'), True)

    def test_20(self):
        sol = Solution()
        self.assertEqual(sol.isNumber('4e+'), False)

    def test_21(self):
        sol = Solution()
        self.assertEqual(sol.isNumber('378510e004'), True)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_20()
