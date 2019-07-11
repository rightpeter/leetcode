#!/usr/bin/env python3

from typing import List


class Solution:
    def maxSubArray(self, nums: 'List[int]') -> 'int':
        max_num = max(nums)

        if max_num <= 0:
            return max_num

        res = nums[0]
        tmp_sum = 0

        for num in nums:
            tmp_sum = max(0, tmp_sum + num)
            res = max(res, tmp_sum)

        return res
