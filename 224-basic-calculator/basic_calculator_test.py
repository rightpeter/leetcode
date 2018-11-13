#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from basic_calculator import Solution


class TestCalculator(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.calculate("1 + 1"), 2)

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.calculate("2-1 + 2 "), 3)

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.calculate("(1+(4+5+2)-3)+(6+8)"), 23)

    def test_4(self):
        sol = Solution()
        self.assertEqual(sol.calculate("()"), 0)

    def test_5(self):
        sol = Solution()
        self.assertEqual(sol.calculate("(2)"), 2)

    def test_6(self):
        sol = Solution()
        self.assertEqual(sol.calculate("3"), 3)

    def test_7(self):
        sol = Solution()
        self.assertEqual(sol.calculate("(7)-(0)+(4)"), 11)

    def test_8(self):
        sol = Solution()
        self.assertEqual(sol.calculate("(2+5)-(0)+(2+2)"), 11)

    def test_9(self):
        sol = Solution()
        self.assertEqual(sol.calculate("(6)-(8)-(7)+(1+(6))"), -2)


if __name__ == '__main__':
    unittest.main()
    # TestCalculator().test_9()
