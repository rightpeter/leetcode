#!/usr/bin/env python3

from typing import List


class Solution:

    def maxArea(self, height: List[int]) -> int:
        max_S = 0
        n = len(height)

        for i in range(0, n - 1):
            for j in range(i + 1, n):
                S = min(height[i], height[j]) * (j - i)
                max_S = max(max_S, S)

        return max_S
