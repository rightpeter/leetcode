#!/usr/bin/env python3


class Solution:

    def numDecodings(self, s: str) -> int:
        n = len(s)

        if n == 0:
            return 0

        dp = [0 for _ in range(n + 1)]

        dp[n] = 1
        if s[n - 1] == '0':
            dp[n - 1] = 0
        else:
            dp[n - 1] = 1

        for i in range(n - 2, -1, -1):
            if s[i] == '0':
                dp[i] = 0
                continue

            dp[i] = dp[i + 1]
            if s[i] == '1' or s[i] == '2' and s[i + 1] in {
                    '0', '1', '2', '3', '4', '5', '6'
            }:
                dp[i] += dp[i + 2]

        return dp[0]
