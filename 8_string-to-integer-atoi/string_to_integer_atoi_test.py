#!/usr/bin/env python3

import unittest
from string_to_integer_atoi import Solution


class TestStringToIntegerAtoi(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.myAtoi("42"), 42)

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.myAtoi("   -42"), -42)

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.myAtoi("4193 with words"), 4193)

    def test_4(self):
        sol = Solution()
        self.assertEqual(sol.myAtoi("words and 987"), 0)

    def test_5(self):
        sol = Solution()
        self.assertEqual(sol.myAtoi("-91283472332"), -2147483648)

    def test_6(self):
        sol = Solution()
        self.assertEqual(sol.myAtoi(""), 0)

    def test_7(self):
        sol = Solution()
        self.assertEqual(sol.myAtoi("       "), 0)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
