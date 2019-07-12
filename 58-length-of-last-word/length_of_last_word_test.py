#!/usr/bin/env python3

import unittest
from length_of_last_word import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.lengthOfLastWord('Hello World'), 5)

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.lengthOfLastWord('HellosWorld'), 11)

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.lengthOfLastWord(''), 0)

    def test_4(self):
        sol = Solution()
        self.assertEqual(sol.lengthOfLastWord('a'), 1)

    def test_5(self):
        sol = Solution()
        self.assertEqual(sol.lengthOfLastWord('a '), 1)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
