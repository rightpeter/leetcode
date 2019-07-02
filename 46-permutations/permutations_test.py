#!/usr/bin/env python3

import unittest
from permutations import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.permute([1, 2, 3]), [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.permute([1, 2]), [[1, 2], [2, 1]])

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.permute([]), [])

    def test_4(self):
        sol = Solution()
        self.assertEqual(sol.permute([1]), [[1]])

    def test_5(self):
        sol = Solution()
        self.assertEqual(sol.permute([9, 3, 6, 2]),
                         [[9, 3, 6, 2], [9, 3, 2, 6], [9, 6, 3, 2], [9, 6, 2, 3], [9, 2, 3, 6], [9, 2, 6, 3],
                          [3, 9, 6, 2], [3, 9, 2, 6], [3, 6, 9, 2], [3, 6, 2, 9], [3, 2, 9, 6], [3, 2, 6, 9],
                          [6, 9, 3, 2], [6, 9, 2, 3], [6, 3, 9, 2], [6, 3, 2, 9], [6, 2, 9, 3], [6, 2, 3, 9],
                          [2, 9, 3, 6], [2, 9, 6, 3], [2, 3, 9, 6], [2, 3, 6, 9], [2, 6, 9, 3], [2, 6, 3, 9]])


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
