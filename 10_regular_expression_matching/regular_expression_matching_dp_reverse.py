#!/usr/bin/env python3


class Solution:

    def isMatch(self, s, p):
        # print("isMatch, s: {}, p: {}".format(s, p))
        dp = [[False for i in range(len(p) + 1)] for j in range(len(s) + 1)]

        dp[len(s)][len(p)] = True

        for i in range(len(s), -1, -1):
            for j in range(len(p) - 1, -1, -1):
                if j + 1 < len(p) and p[j + 1] == '*':
                    dp[i][j] = i < len(s) and p[j] in {s[i], '.'} and dp[i + 1][j] or dp[i][j + 2]
                else:
                    dp[i][j] = i < len(s) and p[j] in {s[i], '.'} and dp[i + 1][j + 1]

        # for i in dp:
        # print(i)
        return dp[0][0]
