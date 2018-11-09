#!/usr/bin/env python3


class Solution:

    def isMatch(self, s, p):
        # print("isMatch, s: {}, p: {}".format(s, p))
        dp = [[False for i in range(len(p) + 1)] for j in range(len(s) + 1)]
        dp[0][0] = True

        for i in range(len(s) + 1):
            for j in range(1, len(p) + 1):
                if i > 0 and p[j - 1] in {s[i - 1], '.'}:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = i > 0 and p[j - 2] in {s[i - 1], '.'} and dp[i - 1][j] or dp[i][j - 2]

        # for i in dp:
            # print(i)
        return dp[len(s)][len(p)]
