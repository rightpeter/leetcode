#!/usr/bin/env python3

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        if n == 0:
            return 0

        res = heights[0]

        stack = [-1 for _ in range(n + 1)]
        top = 0
        for i in range(n):
            if top <= 0 or heights[stack[top]] <= heights[i]:
                top += 1
                stack[top] = i
            else:
                while top > 0 and heights[stack[top]] > heights[i]:
                    res = max(heights[stack[top]] * (i - stack[top - 1] - 1), res)
                    top -= 1

                top += 1
                stack[top] = i

        while top > 0:
            res = max(heights[stack[top]] * (n - stack[top - 1] - 1), res)
            top -= 1

        return res
