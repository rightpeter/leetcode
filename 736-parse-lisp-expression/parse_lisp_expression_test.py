#!/usr/bin/env python3

import unittest
from parse_lisp_expression import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.evaluate("(add 1 2)"), 3)

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.evaluate("(mult 3 (add 2 3))"), 15)

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.evaluate("(let x 2 (mult x 5))"), 10)

    def test_4(self):
        sol = Solution()
        self.assertEqual(
            sol.evaluate("(let x 2 (mult x (let x 3 y 4 (add x y))))"), 14)

    def test_5(self):
        sol = Solution()
        self.assertEqual(sol.evaluate("(let x 3 x 2 x)"), 2)

    def test_6(self):
        sol = Solution()
        self.assertEqual(sol.evaluate("(let x 1 y 2 x (add x y) (add x y))"), 5)

    def test_7(self):
        sol = Solution()
        self.assertEqual(
            sol.evaluate("(let x 2 (add (let x 3 (let x 4 x)) x))"), 6)

    def test_8(self):
        sol = Solution()
        self.assertEqual(sol.evaluate("(let a1 3 b2 (add a1 1) b2)"), 4)

    def test_9(self):
        sol = Solution()
        self.assertEqual(sol.evaluate("(let x 7 -12)"), -12)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_3()
