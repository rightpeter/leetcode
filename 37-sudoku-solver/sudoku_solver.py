#!/usr/bin/env python3

from typing import List


def print_2_dim_list(list_to_print):
    print('\n'.join([
        ''.join(['{:4}'.format(item) for item in row]) for row in list_to_print
    ]))


class Solution:
    def index_to_square(self, i, j: int) -> int:
        row = int(i / 3)
        col = int(j / 3)

        return 3 * row + col

    def next_slot(self, i, j: int) -> List[int]:
        # print(f'next_slot i: {i}, j: {j}')
        if i == 8 and j == 8:
            return [-1, -1]

        if j == 8:
            return [i + 1, 0]
        else:
            return [i, j + 1]

    def next_empty_slot(self, i, j: int) -> List[int]:
        if self.board[i][j] == '.':
            return [i, j]

        x, y = self.next_slot(i, j)

        if x == y == -1:
            return [-1, -1]

        while self.board[x][y] != '.':
            x, y = self.next_slot(x, y)
            if x == y == -1:
                return [-1, -1]

        return [x, y]

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board

        col_set = [[True for _ in range(9)] for _ in range(9)]
        self.col_set = col_set
        row_set = [[True for _ in range(9)] for _ in range(9)]
        self.row_set = row_set
        square_set = [[True for _ in range(9)] for _ in range(9)]
        self.square_set = square_set

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    col_set[j][int(board[i][j]) - 1] = False
                    row_set[i][int(board[i][j]) - 1] = False
                    square_set[self.index_to_square(i, j)][int(board[i][j]) -
                                                           1] = False

        i, j = self.next_empty_slot(0, 0)
        self.dfs(i, j)

    def dfs(self, i, j) -> bool:
        for ii in range(9):
            # print(f'ii: {ii}')
            if self.col_set[j][ii] and self.row_set[i][ii] and self.square_set[
                    self.index_to_square(i, j)][ii]:
                self.board[i][j] = str(ii + 1)
                self.col_set[j][ii] = False
                self.row_set[i][ii] = False
                self.square_set[self.index_to_square(i, j)][ii] = False

                # print(f'dfs    i: {i}, j: {j}')
                x, y = self.next_empty_slot(i, j)
                # print(f'new x: {x}, y: {y}')

                if x == y == -1:
                    return True

                # print_2_dim_list(self.board)
                # print(f'dfs! i: {i}, j: {j}')
                solved = self.dfs(x, y)

                if solved:
                    return True

                self.board[i][j] = '.'
                self.col_set[j][ii] = True
                self.row_set[i][ii] = True
                self.square_set[self.index_to_square(i, j)][ii] = True

        return False
