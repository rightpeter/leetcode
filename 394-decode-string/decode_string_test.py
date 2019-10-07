#!/usr/bin/env python3

import unittest
from decode_string import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.decodeString("3[a]2[bc]"), "aaabcbc")

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.decodeString("3[a2[c]]"), "accaccacc")

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.decodeString("2[abc]3[cd]ef"), "abcabccdcdcdef")


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_2()
