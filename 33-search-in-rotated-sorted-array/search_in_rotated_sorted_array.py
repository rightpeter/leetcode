#!/usr/bin/env python3

from typing import List


class Solution:

    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            # print(f'l: {l}, m: {m}, r: {r}')

            if nums[m] == target:
                return m

            if nums[l] < nums[r]:
                # normal bin search
                if target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[l] >  nums[m]:
                    # pivot is in left half part of interval
                    if nums[m] < target <= nums[r]:
                        l = m + 1
                    else:
                        r = m - 1
                else:
                    if nums[l] <= target < nums[m]:
                        r = m - 1
                    else:
                        l = m + 1

        return -1
