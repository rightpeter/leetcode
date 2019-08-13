#!/usr/bin/env python3

import unittest
from decode_ways import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.numDecodings('12'), 2)

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.numDecodings('226'), 3)

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.numDecodings(''), 0)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
