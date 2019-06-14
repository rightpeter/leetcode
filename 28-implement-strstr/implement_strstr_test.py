#!/usr/bin/env python3

import unittest
from implement_strstr import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.strStr('hello', 'll'), 2)

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.strStr('aaaaa', 'bba'), -1)

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.strStr('aaaaa', ''), 0)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
