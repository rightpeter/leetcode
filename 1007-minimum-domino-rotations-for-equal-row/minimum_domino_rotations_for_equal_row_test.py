#!/usr/bin/env python3

import unittest
from minimum_domino_rotations_for_equal_row import Solution


class TestSolution(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        self.assertEqual(
            sol.minDominoRotations([2, 1, 2, 4, 2, 2], [5, 2, 6, 2, 3, 2]), 2)

    def test_2(self):
        sol = Solution()
        self.assertEqual(
            sol.minDominoRotations([3, 5, 1, 2, 3], [3, 6, 3, 3, 4]), -1)

    def test_3(self):
        sol = Solution()
        self.assertEqual(
            sol.minDominoRotations([1, 2, 1, 1, 1, 2, 2, 2],
                                   [2, 1, 2, 2, 2, 2, 2, 2]), 1)

    def test_4(self):
        sol = Solution()
        self.assertEqual(
            sol.minDominoRotations([1, 2, 1, 1, 1, 2, 2, 2],
                                   [2, 1, 2, 2, 2, 2, 2, 2]), 1)

    def test_5(self):
        sol = Solution()
        self.assertEqual(
            sol.minDominoRotations([2, 1, 2, 2, 2, 2], [2, 2, 6, 2, 3, 2]), 1)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
