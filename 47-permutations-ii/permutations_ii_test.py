#!/usr/bin/env python3

import unittest
from permutations_ii import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.permuteUnique([1, 1, 2]), [[1, 1, 2], [1, 2, 1], [2, 1, 1]])

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.permuteUnique([1, 2]), [[1, 2], [2, 1]])

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.permuteUnique([]), [])

    def test_4(self):
        sol = Solution()
        self.assertEqual(sol.permuteUnique([1]), [[1]])

    def test_5(self):
        sol = Solution()
        self.assertEqual(sol.permuteUnique([9, 3, 6, 2]), [
            [2, 3, 6, 9],
            [2, 3, 9, 6],
            [2, 6, 3, 9],
            [2, 6, 9, 3],
            [2, 9, 3, 6],
            [2, 9, 6, 3],
            [3, 2, 6, 9],
            [3, 2, 9, 6],
            [3, 6, 2, 9],
            [3, 6, 9, 2],
            [3, 9, 2, 6],
            [3, 9, 6, 2],
            [6, 2, 3, 9],
            [6, 2, 9, 3],
            [6, 3, 2, 9],
            [6, 3, 9, 2],
            [6, 9, 2, 3],
            [6, 9, 3, 2],
            [9, 2, 3, 6],
            [9, 2, 6, 3],
            [9, 3, 2, 6],
            [9, 3, 6, 2],
            [9, 6, 2, 3],
            [9, 6, 3, 2],
        ])

    def test_6(self):
        sol = Solution()
        self.assertEqual(sol.permuteUnique([2, 2, 2]), [[2, 2, 2]])

    def test_7(self):
        sol = Solution()
        self.assertEqual(
            sol.permuteUnique([2, 2, 3, 3, 5]),
            [[2, 2, 3, 3, 5], [2, 2, 3, 5, 3], [2, 2, 5, 3, 3], [2, 3, 2, 3, 5], [2, 3, 2, 5, 3], [2, 3, 3, 2, 5],
             [2, 3, 3, 5, 2], [2, 3, 5, 2, 3], [2, 3, 5, 3, 2], [2, 5, 2, 3, 3], [2, 5, 3, 2, 3], [2, 5, 3, 3, 2],
             [3, 2, 2, 3, 5], [3, 2, 2, 5, 3], [3, 2, 3, 2, 5], [3, 2, 3, 5, 2], [3, 2, 5, 2, 3], [3, 2, 5, 3, 2],
             [3, 3, 2, 2, 5], [3, 3, 2, 5, 2], [3, 3, 5, 2, 2], [3, 5, 2, 2, 3], [3, 5, 2, 3, 2], [3, 5, 3, 2, 2],
             [5, 2, 2, 3, 3], [5, 2, 3, 2, 3], [5, 2, 3, 3, 2], [5, 3, 2, 2, 3], [5, 3, 2, 3, 2], [5, 3, 3, 2, 2]])


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_5()
