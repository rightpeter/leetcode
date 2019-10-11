#!/usr/bin/env python3

from typing import List


class Solution:

    def splitArray(self, nums: List[int], m: int) -> int:
        avg = sum(nums) / m
        lo = int(avg)

        hi = 0
        i = 0
        while i < len(nums):
            tsum = nums[i]
            while i + 1 < len(nums) and tsum < avg:
                i += 1
                tsum += nums[i]
            i += 1
            hi = max(hi, tsum)

        while lo <= hi:
            mid = (lo + hi) // 2

            count = 0
            i = 0
            valid = True
            while i < len(nums) and valid:
                tsum = 0
                while i < len(nums) and tsum + nums[i] <= mid:
                    tsum += nums[i]
                    i += 1

                if i < len(nums) and nums[i] > mid:
                    valid = False

                count += 1

            if valid and count > m:
                valid = False

            if valid:
                hi = mid - 1
            else:
                lo = mid + 1

        return lo
