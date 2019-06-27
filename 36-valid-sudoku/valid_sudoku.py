#!/usr/bin/env python3

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # column and row
        for i in range(9):
            col_set = set()
            row_set = set()

            for j in range(9):
                if board[j][i] in col_set:
                    return False
                else:
                    if board[j][i] != '.':
                        col_set.add(board[j][i])

                if board[i][j] in row_set:
                    return False
                else:
                    if board[i][j] != '.':
                        row_set.add(board[i][j])

        for i in range(3):
            for j in range(3):
                square_set = set()

                for ii in range(3*i, 3*i + 3):
                    for jj in range(3*j, 3*j + 3):
                        if board[ii][jj] in square_set:
                            return False
                        else:
                            if board[ii][jj] != '.':
                                square_set.add(board[ii][jj])

        return True
