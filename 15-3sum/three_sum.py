#!/usr/bin/env python3

from typing import List


def two_sum(nums: List[int], target, n, l: int) -> List[List[int]]:
    j = n - 1
    i = l
    res = []

    while i < j:
        tmp = nums[i] + nums[j]

        if tmp == target:
            res.append((nums[i], nums[j]))
            i += 1
        if tmp > target:
            j -= 1

        if tmp < target:
            i += 1

    return res


class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []

        nums = sorted(nums)
        prev = nums[0] - 1
        count = 0
        new_nums = []

        for num in nums:
            if num == prev:
                count += 1
            else:
                if prev == 0:
                    limit = 3
                else:
                    limit = 2

                new_nums += min(count, limit) * [prev]
                prev = num
                count = 1

        if prev == 0:
            limit = 3
        else:
            limit = 2

        new_nums += min(count, limit) * [prev]

        fix_set = set()
        sum_set = set()

        nums = new_nums
        n = len(nums)

        res = []

        for i in range(0, n - 2):
            if nums[i] > 0:
                break

            if nums[i] not in fix_set:
                ts = two_sum(nums, -nums[i], n, i + 1)

                for t in ts:
                    if t not in sum_set:
                        res.append([nums[i], t[0], t[1]])
                        sum_set.add(t)

                fix_set.add(nums[i])

        return res
