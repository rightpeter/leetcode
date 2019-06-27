#!/usr/bin/env python3

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = []

        l = 0
        r = len(nums) - 1
        mid = -1

        while l <= r:
            m = int((l + r) / 2)

            if nums[m] == target:
                mid = m
                break
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        if mid == -1:
            return [-1, -1]

        right = r

        # find left end
        r = mid
        while l <= r:
            m = int((l + r) / 2)

            if nums[m] == target and (m == 0 or nums[m - 1] != target):
                res.append(m)
                break
            elif nums[m] == target:
                r = m - 1
            else:
                l = m + 1

        # find right end
        l = mid
        r = right
        while l <= r:
            m = int((l + r) / 2)

            if nums[m] == target and (m == len(nums) - 1
                                      or nums[m + 1] != target):
                res.append(m)
                break
            elif nums[m] == target:
                l = m + 1
            else:
                r = m - 1

        return res
