#!/usr/bin/env python3

from typing import List

class Solution:

    def nextPermutation(self, nums: List[int]) -> None:
        if len(nums) <= 1:
            return

        i = len(nums) - 1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1

        if i == 0:
            nums.reverse()
            return
        else:
            i -= 1
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
            nums[i+1:] = reversed(nums[i+1:])
