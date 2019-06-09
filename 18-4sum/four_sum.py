#!/usr/bin/env python3

from typing import List


class Solution:

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []

        nums = sorted(nums)
        n = len(nums)

        res = []
        i = 0
        for i in range(0, n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] + 3 * nums[-1] < target:
                continue
            if nums[i] * 4 > target:
                continue

            for j in range(i+1, n-2):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                if nums[i] + nums[j] + 2 * nums[-1] < target:
                    continue
                if nums[i] + 3 * nums[j] > target:
                    continue

                l = j + 1
                r = n - 1
                tmp_target = target - nums[i] - nums[j]
                while l < r:
                    if nums[l] + nums[r] > tmp_target:
                        r -= 1
                    elif nums[l] + nums[r] < tmp_target:
                        l += 1
                    else:
                        if l == j + 1 or nums[l] != nums[l - 1]:
                            res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1

        return res
