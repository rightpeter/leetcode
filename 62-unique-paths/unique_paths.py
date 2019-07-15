#!/usr/bin/env python3


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 0

        dp = [1 for _ in range(m)]

        for r in range(1, n):
            for c in range(1, m):
                dp[c] += dp[c - 1]

        return dp[-1]
