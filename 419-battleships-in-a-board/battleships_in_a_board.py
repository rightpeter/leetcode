#!/usr/bin/env python3

from typing import List


class Solution:

    def countBattleships(self, board: List[List[str]]) -> int:
        res = 0
        n = len(board)
        if not n:
            return 0

        m = len(board[0])
        if not m:
            return 0

        for i in range(n):
            j = 0
            while j < m:
                if board[i][j] == '.':
                    j += 1
                    continue

                if board[i][j] == 'X' and (i == 0 or board[i - 1][j] == '.'):
                    res += 1

                while j + 1 < m and board[i][j + 1] == 'X':
                    j += 1

                j += 1

        return res
