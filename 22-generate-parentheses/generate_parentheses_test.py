#!/usr/bin/env python3

import unittest
from generate_parentheses import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.generateParenthesis(3), ['()()()', '()(())', '(())()', '(()())', '((()))'])

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.generateParenthesis(2), ['()()', '(())'])

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.generateParenthesis(0), [])

    def test_4(self):
        sol = Solution()
        self.assertEqual(sol.generateParenthesis(1), ['()'])


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
