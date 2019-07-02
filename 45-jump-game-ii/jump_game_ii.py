#!/usr/bin/env python3

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        curr = len(nums)

        if curr == 1:
            return 0
        elif max(nums) <= 1:
            return len(nums) - 1

        while curr > 1:
            # print(f'res: {res}, curr: {curr}')
            for i in range(curr):
                if i + nums[i] >= curr - 1:
                    curr = i + 1
                    res += 1
                    break

        return res
