#!/usr/bin/env python3

import copy
from typing import List


class Solution:
    def availability_list_update(self, i, j: int) -> List[List[int]]:
        def diagonal(i, j):
            if 0 <= i < self.n and 0 <= j < self.n and self.availability[i][j]:
                update_list.append([i, j])

        update_list = []

        for x in range(self.n):
            if self.availability[x][j]:
                update_list.append([x, j])

            if self.availability[i][x]:
                update_list.append([i, x])

            ni = i - x
            pi = i + x
            nj = j - x
            pj = j + x

            # ↖ (ni, nj)
            diagonal(ni, nj)

            # ↗ (ni, pj)
            diagonal(ni, pj)

            # ↘ (pi, pj)
            diagonal(pi, pj)

            # ↙ (pi, nj)
            diagonal(pi, nj)

        return update_list

    def dfs(self, step: int):
        if step == self.n:
            # print(f'------------ dfs: {step} ------------')
            # for line in self.board:
                # print(line)

            tmp_board = []
            for line in self.board:
                tmp_board.append(''.join(line))

            self.res.append(tmp_board)
            return

        for j in range(self.n):
            if self.availability[step][j]:
                self.board[step][j] = 'Q'
                update_list = self.availability_list_update(step, j)
                for x, y in update_list:
                    self.availability[x][y] = False

                self.dfs(step + 1)

                for x, y in update_list:
                    self.availability[x][y] = True
                self.board[step][j] = '.'

    def solveNQueens(self, n: int) -> List[List[str]]:
        if n <= 0:
            return []

        self.n = n
        self.res = []
        self.board = [['.' for _ in range(n)] for _ in range(n)]
        self.availability = [[True for _ in range(n)] for _ in range(n)]
        self.dfs(0)

        return self.res
