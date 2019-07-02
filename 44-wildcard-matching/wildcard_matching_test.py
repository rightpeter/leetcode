#!/usr/bin/env python3

import unittest
from wildcard_matching import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.isMatch('aa', 'a'), False)

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.isMatch('aa', '*'), True)

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.isMatch('cb', '?a'), False)

    def test_4(self):
        sol = Solution()
        self.assertEqual(sol.isMatch('adceb', '*a*b'), True)

    def test_5(self):
        sol = Solution()
        self.assertEqual(sol.isMatch('acdcb', 'a*c?b'), False)

    def test_6(self):
        sol = Solution()
        self.assertEqual(sol.isMatch('a', 'ab?'), False)

    def test_7(self):
        sol = Solution()
        self.assertEqual(sol.isMatch('a', '*?'), True)

    def test_8(self):
        sol = Solution()
        self.assertEqual(sol.isMatch('', ''), True)

    def test_9(self):
        sol = Solution()
        self.assertEqual(sol.isMatch('', 'a'), False)

    def test_10(self):
        sol = Solution()
        self.assertEqual(sol.isMatch('a', ''), False)

    def test_11(self):
        sol = Solution()
        self.assertEqual(sol.isMatch('mississippi', 'm??*ss*?i*pi'), False)

    def test_12(self):
        sol = Solution()
        self.assertEqual(sol.isMatch('', '*'), True)

    def test_13(self):
        sol = Solution()
        self.assertEqual(sol.isMatch('ho', '**ho'), True)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_12()
