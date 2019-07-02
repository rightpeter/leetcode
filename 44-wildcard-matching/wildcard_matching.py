#!/usr/bin/env python3


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ns = len(s)
        np = len(p)

        if ns == np == 0:
            return True
        elif np == 0:
            return False

        dp = [[False for _ in range(np + 1)] for _ in range(ns + 1)]

        dp[0][0] = True

        for l2 in range(0, np):
            if p[l2] == '*':
                start = 0
                while start <= ns and not dp[start][l2]:
                    start += 1

                for i in range(start, ns + 1):
                    dp[i][l2 + 1] = True
            else:
                for l1 in range(0, ns):
                    if p[l2] == '?':
                        dp[l1 + 1][l2 + 1] = dp[l1][l2]
                    else:
                        dp[l1 + 1][l2 + 1] = dp[l1][l2] and s[l1] == p[l2]

        # print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in dp]))
        return dp[ns][np]
