#!/usr/bin/env python3

import unittest
from valid_palindrome import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(
            sol.isPalindrome("A man, a plan, a canal: Panama"), True)

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.isPalindrome("race a car"), False)

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.isPalindrome(""), True)

    def test_4(self):
        sol = Solution()
        self.assertEqual(sol.isPalindrome("0P"), False)


if __name__ == '__main__':
    # unittest.main()
    TestSolution().test_4()
