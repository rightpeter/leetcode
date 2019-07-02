#!/usr/bin/env python3

from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []

        nums = sorted(nums)

        res = []
        n = len(nums)
        used = [False for _ in range(len(nums))]

        def dfs(path: List[int]):
            if len(path) == n:
                res.append(path)

            for i in range(n):
                if not used[i] and (i == 0 or nums[i - 1] != nums[i] or used[i - 1]):
                    used[i] = True
                    dfs(path + [nums[i]])
                    used[i] = False

        dfs([])
        # print('\n'.join([str(item) for item in res]))

        return res
