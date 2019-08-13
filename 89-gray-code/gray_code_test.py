#!/usr/bin/env python3

import unittest
from gray_code import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.grayCode(2), [0, 1, 3, 2])

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.grayCode(0), [0])

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.grayCode(1), [0, 1])

    def test_4(self):
        sol = Solution()
        self.assertEqual(sol.grayCode(3), [0, 1, 3, 2, 6, 7, 5, 4])

    def test_5(self):
        sol = Solution()
        self.assertEqual(
            sol.grayCode(4),
            [0, 1, 3, 2, 6, 7, 5, 4, 12, 13, 15, 14, 10, 11, 9, 8])


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_5()
