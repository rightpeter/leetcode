#!/usr/bin/env python3

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
            self.res += 1
            return

        for j in range(self.n):
            if self.row_availability[step] and self.col_availability[
                    j] and self.diag_drop_availability[step - j] and self.diag_rise_availability[step + j]:
                self.row_availability[step] = False
                self.col_availability[j] = False
                self.diag_drop_availability[step - j] = False
                self.diag_rise_availability[step + j] = False

                self.dfs(step + 1)

                self.row_availability[step] = True
                self.col_availability[j] = True
                self.diag_drop_availability[step - j] = True
                self.diag_rise_availability[step + j] = True

    def totalNQueens(self, n: int) -> int:
        self.row_availability = [True for _ in range(n)]
        self.col_availability = [True for _ in range(n)]
        self.diag_drop_availability = [True for _ in range(2 * n - 1)]  # ↘
        self.diag_rise_availability = [True for _ in range(2 * n - 1)]  # ↗

        if n <= 0:
            return 0

        self.n = n
        self.res = 0
        self.dfs(0)

        return self.res
