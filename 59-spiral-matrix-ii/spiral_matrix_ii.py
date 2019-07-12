#!/usr/bin/env python3

from typing import List

direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        def next_step(x, y, seq: int):
            return x + direction[seq][0], y + direction[seq][1]

        def modify_bound(seq):
            nonlocal lr, hc, hr, lc

            if seq == 0:
                lr += 1
            elif seq == 1:
                hc -= 1
            elif seq == 2:
                hr -= 1
            elif seq == 3:
                lc += 1

        def valid_cord(x, y):
            if lr <= x <= hr and lc <= y <= hc:
                return True
            else:
                return False

        board = [[0 for _ in range(n)] for _ in range(n)]

        lr = 0
        hr = n - 1
        lc = 0
        hc = n - 1

        x = y = 0
        seq = 0

        for i in range(1, n**2 + 1):
            board[x][y] = i

            nx, ny = next_step(x, y, seq)
            if not valid_cord(nx, ny):
                modify_bound(seq)
                seq = (seq + 1) % 4
                nx, ny = next_step(x, y, seq)

            x, y = nx, ny

        return board
