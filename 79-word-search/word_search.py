#!/usr/bin/env python3

from typing import List

direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        if n == 0:
            return False
        m = len(board[0])
        if m == 0:
            return False

        available = [[True for _ in range(m)] for _ in range(n)]

        def search_word(x, y, wi: int) -> bool:
            # print('----------------------------------------------------------------------')
            # print(f'x: {x}, y: {y}, wi: {wi}')
            # print('available:')
            # for line in available:
                # print(''.join(['T' if x else 'F' for x in line]))

            if wi >= len(word):
                return True

            for i in range(4):
                nx, ny = x + direction[i][0], y + direction[i][1]
                if 0 <= nx < n and 0 <= ny < m:
                    if available[nx][ny] and board[nx][ny] == word[wi]:
                        # print(f'nx: {nx}, ny: {ny}, c: {word[wi]}')
                        available[nx][ny] = False
                        if search_word(nx, ny, wi + 1):
                            return True
                        available[nx][ny] = True

            return False

        # for line in board:
            # print(''.join(line))

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    available[i][j] = False
                    if search_word(i, j, 1):
                        return True
                    available[i][j] = True

        return False
