#!/usr/bin/env python3

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = len(nums) - 1

        for r in range(len(nums)):
            if nums[r] == 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1

        r = len(nums) - 1

        while l < r:
            # print(f'l: {l}, r: {r}, nums: {nums}')
            while l < r and nums[l] == 1:
                # print(f'left, l: {l}, r: {r}')
                l += 1
            while l < r and nums[r] == 2:
                # print(f'right, l: {l}, r: {r}')
                r -= 1

            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        # print(f'l: {l}, r: {r}, nums: {nums}')
