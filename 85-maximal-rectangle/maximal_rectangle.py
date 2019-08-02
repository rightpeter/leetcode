#!/usr/bin/env python3

from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        if n == 0:
            return 0

        m = len(matrix[0])
        if m == 0:
            return 0

        histograms = [[0 for _ in range(m)] for _ in range(n)]

        for j in range(m):
            if matrix[0][j] == '1':
                histograms[0][j] = 1

        for i in range(1, n):
            for j in range(m):
                if matrix[i][j] == '0':
                    histograms[i][j] = 0
                else:
                    histograms[i][j] = histograms[i - 1][j] + 1

        # for line in histograms:
            # print(line)
        # print()

        res = histograms[0][0]

        stack = [-1 for _ in range(m + 1)]
        for line in histograms:
            top = 0
            for j in range(m):
                if top == 0 or line[stack[top]] <= line[j]:
                    top += 1
                    stack[top] = j
                elif line[stack[top]] > line[j]:
                    while top > 0 and line[stack[top]] > line[j]:
                        # if line[stack[top]] * (j - stack[top - 1] - 1) == 6:
                            # print('sum is 6')
                            # print(f'line: {line}\nstack: {stack}\ntop: {top}, j: {j}')
                        res = max(line[stack[top]] * (j - stack[top - 1] - 1), res)
                        top -= 1
                    top += 1
                    stack[top] = j
            while top > 0:
                res = max(line[stack[top]] * (m - stack[top - 1] - 1), res)
                top -= 1

        return res
