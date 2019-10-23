#!/usr/bin/env python3

import unittest
from find_all_anagrams_in_a_string import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.findAnagrams("cbaebabacd", "abc"), [0, 6])

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.findAnagrams("abab", "ab"), [0, 1, 2])

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.findAnagrams("acac", "ab"), [])

    def test_4(self):
        sol = Solution()
        self.assertEqual(sol.findAnagrams("a", "ab"), [])

    def test_5(self):
        sol = Solution()
        self.assertEqual(sol.findAnagrams("", "ab"), [])

    def test_6(self):
        sol = Solution()
        self.assertEqual(
            sol.findAnagrams("aaaaaaaaa", "a"), [0, 1, 2, 3, 4, 5, 6, 7, 8])


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
