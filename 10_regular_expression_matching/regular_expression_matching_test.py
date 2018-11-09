#!/usr/bin/env python3

import unittest
from regular_expression_matching_dp_reverse import Solution


class TestReExpress(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.isMatch("aa", "a"), False)

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.isMatch("aa", "a*"), True)

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.isMatch("ab", ".*"), True)

    def test_4(self):
        sol = Solution()
        self.assertEqual(sol.isMatch("mississippi", "mis*is*p*."), False)

    def test_5(self):
        sol = Solution()
        self.assertEqual(sol.isMatch("mississippi", "mis*is*ip*."), True)

    def test_6(self):
        sol = Solution()
        self.assertEqual(sol.isMatch("N", "p*p"), False)

    def test_7(self):
        sol = Solution()
        self.assertEqual(sol.isMatch("SpN", "Sp*pN"), True)

    def test_8(self):
        sol = Solution()
        self.assertEqual(sol.isMatch("SN", "Sp*pN"), False)

    def test_9(self):
        sol = Solution()
        self.assertEqual(sol.isMatch("SN", "Sp*N"), True)

    def test_10(self):
        sol = Solution()
        self.assertEqual(sol.isMatch("aaa", "a*a"), True)

    def test_11(self):
        sol = Solution()
        self.assertEqual(sol.isMatch("aaa", "ab*a*c*a"), True)

    def test_12(self):
        sol = Solution()
        self.assertEqual(sol.isMatch("aa", "a*aa"), True)

    def test_13(self):
        sol = Solution()
        self.assertEqual(sol.isMatch("aa", "a*aaa"), False)

    def test_14(self):
        sol = Solution()
        self.assertEqual(sol.isMatch("bbbba", ".*a*a"), True)

    def test_15(self):
        sol = Solution()
        self.assertEqual(sol.isMatch("", ".*"), True)

if __name__ == '__main__':
    unittest.main()
    # TestReExpress().test_6()
