#!/usr/bin/env python3

import unittest
from roman_to_integer import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.romanToInt("III"), 3)

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.romanToInt("IV"), 4)

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.romanToInt("IX"), 9)

    def test_4(self):
        sol = Solution()
        self.assertEqual(sol.romanToInt("LVIII"), 58)

    def test_5(self):
        sol = Solution()
        self.assertEqual(sol.romanToInt("MCMXCIV"), 1994)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
