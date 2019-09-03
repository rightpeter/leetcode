#!/usr/bin/env python3

from typing import List
from bisect import bisect_left


class Solution:

    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        dp = [0] * n

        dp[0] = nums[0]
        p = 0

        for num in nums[1:]:
            if num > dp[p]:
                p += 1
                dp[p] = num
            else:
                i = bisect_left(dp, num, hi=p + 1)
                dp[i] = num

        return p + 1
