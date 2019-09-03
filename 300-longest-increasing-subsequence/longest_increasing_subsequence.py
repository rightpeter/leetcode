#!/usr/bin/env python3

from typing import List


class Solution:

    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        dp = [1] * n

        res = 1
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

                res = max(res, dp[i])
        return res
