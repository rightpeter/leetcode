#!/usr/bin/env python3

from typing import List


class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        duplicate = {}
        if n < 2:
            return []

        nums = sorted(nums)

        nums_dict = {}
        prev = nums[0] - 1
        count = 0
        new_nums = []
        for num in nums:
            if num == prev and count < 3:
                count += 1
            if num != prev:
                nums_dict[prev] = count
                new_nums += count * [prev]
                count = 1
                prev = num

        nums_dict[prev] = count
        new_nums += count * [prev]

        nums = new_nums
        n = len(nums)
        # print(f'nums: {nums}')
        # print(f'nums_dict: {nums_dict}')

        res = []

        for i in range(0, n - 2):
            nums_dict[nums[i]] = nums_dict[nums[i]] - 1
            for j in range(i + 1, n - 1):
                nums_dict[nums[j]] = nums_dict[nums[j]] - 1
                c = -nums[i] - nums[j]

                # print(f'nums[i]: {nums[i]}, nums[j]: {nums[j]}, nums_dict: {nums_dict}')
                if not duplicate.get((nums[i], nums[j]), False) and c >= nums[j] and nums_dict.get(c, 0) > 0:
                    res.append([nums[i], nums[j], c])
                    duplicate[(nums[i], nums[j])] = True

                nums_dict[nums[j]] = nums_dict[nums[j]] + 1
            nums_dict[nums[i]] = nums_dict[nums[i]] + 1
        return res
