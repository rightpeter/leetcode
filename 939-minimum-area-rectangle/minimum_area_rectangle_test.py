#!/usr/bin/env python3

import unittest
from minimum_area_rectangle import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(
            sol.minAreaRect([[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]]), 4)

    def test_2(self):
        sol = Solution()
        self.assertEqual(
            sol.minAreaRect([[1, 1], [1, 3], [3, 1], [3, 3], [4, 1], [4, 3]]),
            2)

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.minAreaRect([[1, 1], [1, 3], [3, 1]]), 0)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
