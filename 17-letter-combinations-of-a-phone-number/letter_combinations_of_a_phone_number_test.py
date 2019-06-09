#!/usr/bin/env python3

import unittest
from letter_combinations_of_a_phone_number import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.letterCombinations("23"), ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.letterCombinations(""), [])

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.letterCombinations("3"), ['d', 'e', 'f'])


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
