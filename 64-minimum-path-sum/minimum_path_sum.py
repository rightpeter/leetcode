#!/usr/bin/env python3

from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 0:
            return 0
        m = len(grid[0])
        if m == 0:
            return 0

        dp = [0 for _ in range(m)]
        dp[0] = grid[0][0]

        for c in range(1, m):
            dp[c] = dp[c - 1] + grid[0][c]

        for r in range(1, n):
            dp[0] += grid[r][0]

            for c in range(1, m):
                dp[c] = min(dp[c - 1], dp[c]) + grid[r][c]

        return dp[-1]
