#!/usr/bin/env python3

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        if 1 not in nums:
            return 1
        else:
            for i in range(n):
                if nums[i] <= 0 or nums[i] > n:
                    nums[i] = 1

        for num in nums:
            i = abs(num) - 1
            nums[i] = -1 * abs(nums[i])

        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1
