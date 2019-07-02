#!/usr/bin/env python3

import unittest
from multiply_strings import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.multiply('2', '3'), '6')

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.multiply('123', '456'), '56088')

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.multiply('1234567', '9'), '11111103')

    def test_4(self):
        sol = Solution()
        self.assertEqual(sol.multiply('0', '0'), '0')

    def test_5(self):
        sol = Solution()
        self.assertEqual(sol.multiply('9', '1234567'), '11111103')

    def test_6(self):
        sol = Solution()
        self.assertEqual(sol.multiply('9133', '0'), '0')


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_4()
