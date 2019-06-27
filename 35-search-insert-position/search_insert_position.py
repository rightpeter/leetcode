#!/usr/bin/env python3

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not len(nums):
            return 0

        l = 0
        r = len(nums) - 1

        while l <= r:
            m = int((l + r) / 2)

            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        if r < 0:
            return 0

        if l >= len(nums):
            return len(nums)

        return l
