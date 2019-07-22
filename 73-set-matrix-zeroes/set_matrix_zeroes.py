#!/usr/bin/env python3

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n == 0:
            return matrix

        m = len(matrix[0])

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    for k in range(m):
                        if matrix[i][k] != 0:
                            matrix[i][k] = int(matrix[i][k]) + 0.5

                    for k in range(n):
                        if matrix[k][j] != 0:
                            matrix[k][j] = int(matrix[k][j]) + 0.5

        for i in range(n):
            for j in range(m):
                if int(matrix[i][j]) != matrix[i][j]:
                    matrix[i][j] = 0
