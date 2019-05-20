#!/usr/bin/env python3

import unittest
from integer_to_roman import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.intToRoman(3), "III")

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.intToRoman(4), "IV")

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.intToRoman(9), "IX")

    def test_4(self):
        sol = Solution()
        self.assertEqual(sol.intToRoman(58), "LVIII")

    def test_5(self):
        sol = Solution()
        self.assertEqual(sol.intToRoman(1994), "MCMXCIV")

    def test_6(self):
        sol = Solution()
        self.assertEqual(sol.intToRoman(1400), "MCD")


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
