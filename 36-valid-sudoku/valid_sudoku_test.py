#!/usr/bin/env python3

import unittest
from valid_sudoku import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        self.assertEqual(
            sol.isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."],
                               ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                               [".", "9", "8", ".", ".", ".", ".", "6", "."],
                               ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                               ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                               ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                               [".", "6", ".", ".", ".", ".", "2", "8", "."],
                               [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                               [".", ".", ".", ".", "8", ".", ".", "7", "9"]]),
            True)

    def test_2(self):
        sol = Solution()
        self.assertEqual(
            sol.isValidSudoku([["8", "3", ".", ".", "7", ".", ".", ".", "."],
                               ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                               [".", "9", "8", ".", ".", ".", ".", "6", "."],
                               ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                               ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                               ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                               [".", "6", ".", ".", ".", ".", "2", "8", "."],
                               [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                               [".", ".", ".", ".", "8", ".", ".", "7", "9"]]),
            False)


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_1()
