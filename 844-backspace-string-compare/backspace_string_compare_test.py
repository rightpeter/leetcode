#!/usr/bin/env python3

import unittest
from backspace_string_compare import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.backspaceCompare("ab#c", "ad#c"), True)

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.backspaceCompare("ab##", "c#d#"), True)

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.backspaceCompare("a##c", "#a#c"), True)

    def test_4(self):
        sol = Solution()
        self.assertEqual(sol.backspaceCompare("a#c", "b"), False)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
