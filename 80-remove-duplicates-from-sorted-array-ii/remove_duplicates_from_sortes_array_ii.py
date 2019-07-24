#!/usr/bin/env python3

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        r = 0
        n = len(nums)
        if n == 0:
            return 0

        curr = nums[0] - 1
        count = 1
        while r < n:
            if nums[r] != curr:
                curr = nums[r]
                count = 1
            else:
                count += 1

            if count <= 2:
                # print(f'l: {l}, r: {r}, nums: {nums}')
                nums[l] = nums[r]
                l += 1

            r += 1

        return l
