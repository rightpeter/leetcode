#!/usr/bin/env python3

import unittest
from scramble_string import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.isScramble('great', 'rgeat'), True)

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.isScramble('abcde', 'caebd'), False)

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.isScramble('abb', 'bab'), True)

    def test_4(self):
        sol = Solution()
        self.assertEqual(sol.isScramble('abb', 'bba'), True)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_2()
