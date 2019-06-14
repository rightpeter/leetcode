#!/usr/bin/env python3

from typing import List

class Solution:

    def removeElement(self, nums: List[int], val: int) -> int:
        val_count = 0
        for i in range(len(nums)):
            if nums[i] == val:
                val_count += 1
            else:
                if val_count > 0:
                    nums[i-val_count] = nums[i]
        return len(nums) - val_count
