#!/usr/bin/env python3


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [0 for _ in range(len(word2) + 1)]

        for i in range(1, len(word2) + 1):
            dp[i] = i

        # for i in range(1, len(word1) + 1):
        for c in word1:
            tmp = dp[0]
            dp[0] += 1
            for j in range(1, len(word2) + 1):
                if c != word2[j - 1]:
                    tmp, dp[j] = dp[j], min(dp[j], dp[j - 1], tmp) + 1
                else:
                    tmp, dp[j] = dp[j], min(dp[j], dp[j - 1], tmp - 1) + 1

        return dp[-1]
