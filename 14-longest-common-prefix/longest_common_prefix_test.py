#!/usr/bin/env python3

import unittest
from longest_common_prefix import Solution, twoCommonPrefix


class TestSolution(unittest.TestCase):

    def test_func_1(self):
        self.assertEqual(twoCommonPrefix('aca', 'cba'), '')

    def test_1(self):
        sol = Solution()
        self.assertEqual(
            sol.longestCommonPrefix(["flower", "flow", "flight"]), "fl")

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.longestCommonPrefix(["dog", "racecar", "car"]), "")

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.longestCommonPrefix(["dog"]), "dog")

    def test_4(self):
        sol = Solution()
        self.assertEqual(sol.longestCommonPrefix([]), "")

    def test_5(self):
        sol = Solution()
        self.assertEqual(sol.longestCommonPrefix(["aca", "cba"]), "")


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_func_1()
