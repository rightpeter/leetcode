#!/usr/bin/env python3

from typing import List


class Solution:

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        def dfs(lo, n: int, init: bool) -> List[List[int]]:
            if n == 0:
                return [[]]

            res = []
            if not init:
                res += dfs(lo, n - 1, False)

            for i in range(lo, len(nums) - n + 1):
                if i == lo or nums[i] != nums[i - 1]:
                    res += [[nums[i]] + x for x in dfs(i + 1, n - 1, True)]

            return res

        nums = sorted(nums)

        return dfs(0, len(nums), False)
