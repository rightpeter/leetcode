#!/usr/bin/env python3

from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        if n == 0:
            return 0

        m = len(obstacleGrid[0])
        if m == 0:
            return 0

        if obstacleGrid[0][0] == 1:
            return 0

        dp = [0 for _ in obstacleGrid[0]]
        dp[0] = 1 - obstacleGrid[0][0]
        for c in range(1, m):
            if obstacleGrid[0][c] == 1:
                dp[c] = 0
            else:
                dp[c] = dp[c - 1]

        for r in range(1, n):
            if obstacleGrid[r][0] == 1:
                dp[0] = 0

            for c in range(1, m):
                if obstacleGrid[r][c] == 1:
                    dp[c] = 0
                else:
                    dp[c] += dp[c - 1]

        return dp[-1]
