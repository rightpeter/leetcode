#!/usr/bin/env python3

import unittest
from count_and_say import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.countAndSay(1), '1')

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.countAndSay(4), '1211')


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_3()
