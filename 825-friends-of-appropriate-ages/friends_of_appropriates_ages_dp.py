#!/usr/bin/env python3

from typing import List


class Solution:

    def numFriendRequests(self, ages: List[int]) -> int:
        if not ages:
            return 0

        ages_count = [0] * 121
        dp = [0] * 121

        for age in ages:
            ages_count[age] += 1

        dp[0] = ages_count[0]
        for i in range(1, 121):
            dp[i] = dp[i - 1] + ages_count[i]

        res = 0

        for age in range(1, 121):
            hi = age
            lo = 0.5 * age + 7

            if age > 16:
                res += (dp[hi - 1] - dp[int(lo)]) * ages_count[age]

            if age > 14:
                res += ages_count[age] * (ages_count[age] - 1)

        return res
