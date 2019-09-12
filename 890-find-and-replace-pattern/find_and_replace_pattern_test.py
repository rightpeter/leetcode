#!/usr/bin/env python3

import unittest
from find_and_replace_pattern import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(
            sol.findAndReplacePattern(
                ["abc", "deq", "mee", "aqq", "dkd", "ccc"], "abb"),
            ["mee", "aqq"])

    def test_2(self):
        sol = Solution()
        self.assertEqual(
            sol.findAndReplacePattern(
                ["mee"], "abb"),
            ["mee"])


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_2()
