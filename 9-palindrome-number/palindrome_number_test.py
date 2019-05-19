#!/usr/bin/env python3

import unittest
from palindrome_number import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.isPalindrome(121), True)

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.isPalindrome(-121), False)

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.isPalindrome(0), True)

    def test_4(self):
        sol = Solution()
        self.assertEqual(sol.isPalindrome(345743), False)

    def test_5(self):
        sol = Solution()
        self.assertEqual(sol.isPalindrome(10), False)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
