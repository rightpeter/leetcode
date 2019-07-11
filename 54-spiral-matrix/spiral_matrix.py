#!/usr/bin/env python3

from typing import List

direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]


class Solution:
    def next_step(self, x, y, seq: int):
        return x + direction[seq][0], y + direction[seq][1]

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def modify_boundaries(seq: int):
            nonlocal lr
            nonlocal hr
            nonlocal lc
            nonlocal hc

            if seq == 0:
                lr += 1
            elif seq == 1:
                hc -= 1
            elif seq == 2:
                hr -= 1
            elif seq == 3:
                lc += 1

        n = len(matrix)
        if n == 0:
            return []
        m = len(matrix[0])
        if m == 0:
            return []

        lr = 0
        hr = n - 1
        lc = 0
        hc = m - 1

        res = []
        seq = 0
        x = y = 0

        while True:
            # print(f'x: {x}, y: {y}, seq: {seq}, lr: {lr}, hr: {hr}, lc: {lc}, hc: {hc}')
            res.append(matrix[x][y])
            nx, ny = self.next_step(x, y, seq)
            if lr <= nx <= hr and lc <= ny <= hc:
                x = nx
                y = ny
            else:
                modify_boundaries(seq)
                seq = (seq + 1) % 4
                nx, ny = self.next_step(x, y, seq)
                if lr <= nx <= hr and lc <= ny <= hc:
                    x = nx
                    y = ny
                else:
                    break

        return res
