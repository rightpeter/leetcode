#!/usr/bin/env python3

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def find_previous_step(r: int) -> int:
            res = r
            for i in range(r - 1, -1, -1):
                if i + nums[i] >= r:
                    res = i

            return res

        r = len(nums) - 1
        if r < 0:
            return False

        if max(nums) == 1:
            if 0 in nums[:-1]:
                return False
            else:
                return True

        while True:
            if r == 0:
                return True

            nr = find_previous_step(r)
            if nr == r:
                return False
            else:
                r = nr
