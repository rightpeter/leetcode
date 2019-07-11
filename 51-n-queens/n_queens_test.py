#!/usr/bin/env python3

import unittest
from n_queens import Solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.solveNQueens(4), [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]])

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.solveNQueens(5),
                         [['Q....', '..Q..', '....Q', '.Q...', '...Q.'], ['Q....', '...Q.', '.Q...', '....Q', '..Q..'],
                          ['.Q...', '...Q.', 'Q....', '..Q..', '....Q'], ['.Q...', '....Q', '..Q..', 'Q....', '...Q.'],
                          ['..Q..', 'Q....', '...Q.', '.Q...', '....Q'], ['..Q..', '....Q', '.Q...', '...Q.', 'Q....'],
                          ['...Q.', 'Q....', '..Q..', '....Q', '.Q...'], ['...Q.', '.Q...', '....Q', '..Q..', 'Q....'],
                          ['....Q', '.Q...', '...Q.', 'Q....', '..Q..'], ['....Q', '..Q..', 'Q....', '...Q.', '.Q...']])

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.solveNQueens(1), [["Q"]])

    def test_4(self):
        sol = Solution()
        self.assertEqual(sol.solveNQueens(0), [])


if __name__ == '__main__':
    unittest.main()
    # TestSolution().test_2()
