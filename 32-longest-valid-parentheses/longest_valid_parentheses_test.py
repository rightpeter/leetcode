#!/usr/bin/env python3

import unittest
from longest_valid_parentheses import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.longestValidParentheses('()'), 2)

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.longestValidParentheses('(()'), 2)

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.longestValidParentheses(')()())'), 4)

    def test_4(self):
        sol = Solution()
        self.assertEqual(sol.longestValidParentheses(')(()(()()()()('), 8)

    def test_5(self):
        sol = Solution()
        self.assertEqual(sol.longestValidParentheses('('), 0)

    def test_6(self):
        sol = Solution()
        self.assertEqual(sol.longestValidParentheses(''), 0)

    def test_7(self):
        sol = Solution()
        self.assertEqual(sol.longestValidParentheses(')(((((()())()()))()(()))('), 22)

    def test_8(self):
        sol = Solution()
        self.assertEqual(sol.longestValidParentheses(')()())()()('), 4)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_5()
