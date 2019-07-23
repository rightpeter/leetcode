#!/usr/bin/env python3

import unittest
from minimum_window_substring import Solution


class TestSubstring(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        s = "ADOBECODEBANC"
        t = "ABC"
        self.assertEqual(sol.minWindow(s, t), "BANC")

    def test_2(self):
        sol = Solution()
        s = "ADOBACODEBANC"
        t = "ABC"
        self.assertEqual(sol.minWindow(s, t), "BAC")

    def test_3(self):
        sol = Solution()
        s = "ADOBECODEBAN"
        t = "ABC"
        self.assertEqual(sol.minWindow(s, t), "ADOBEC")

    def test_4(self):
        sol = Solution()
        s = "ADOBECODEBAN"
        t = "ABCX"
        self.assertEqual(sol.minWindow(s, t), "")

    def test_5(self):
        sol = Solution()
        s = "a"
        t = "aa"
        self.assertEqual(sol.minWindow(s, t), "")


if __name__ == '__main__':
    unittest.main()
    # TestSubstring().test_2()
