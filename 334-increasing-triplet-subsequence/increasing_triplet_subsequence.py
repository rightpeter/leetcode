#!/usr/bin/env python3

from typing import List


class Solution:

    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False

        init = False
        small = nums[0]
        large = nums[0]
        tmin = nums[0]

        for num in nums[1:]:
            if not init:
                if num < small:
                    small = num
                    tmin = num

                if num > small:
                    large = num
                    init = True

                continue

            if num > large:
                return True

            if num < tmin:
                tmin = num

            if tmin < num < large:
                small = tmin
                large = num

        return False
