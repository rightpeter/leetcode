#!/usr/bin/env python3

import unittest
from add_binary import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.addBinary('11', '1'), '100')

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.addBinary('1010', '1011'), '10101')

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.addBinary('', ''), '')

    def test_4(self):
        sol = Solution()
        self.assertEqual(sol.addBinary('1011', '111'), '10010')

    def test_5(self):
        sol = Solution()
        self.assertEqual(sol.addBinary('111', '1011'), '10010')

    def test_6(self):
        sol = Solution()
        self.assertEqual(sol.addBinary('1', '10'), '11')


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
