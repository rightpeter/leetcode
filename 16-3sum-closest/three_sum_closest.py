#!/usr/bin/env python3

from typing import List


class Solution:

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        prev = nums[0] - 1
        count = 0
        new_nums = []

        for num in nums:
            if num == prev:
                count += 1
            else:
                new_nums += min(count, 3) * [prev]
                prev = num
                count = 1

        count = min(count, 3)
        new_nums += count * [prev]

        nums = new_nums
        n = len(nums)

        closest = sum(nums[:3])

        for i in range(0, n - 2):
            if nums[i] * 3 - target > abs(closest - target):
                return closest

            l = i + 1
            r = n - 1

            while l < r:
                tmp = nums[i] + nums[l] + nums[r]

                if tmp == target:
                    return target

                if abs(tmp - target) < abs(closest - target):
                    closest = tmp

                if tmp > target:
                    r -= 1
                else:
                    l += 1

        return closest
