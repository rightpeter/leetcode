#!/usr/bin/env python3

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []

        res = []
        n = len(nums)
        used = [False for _ in range(len(nums))]

        def dfs(path: List[int]):
            if len(path) == n:
                res.append(path)

            for i in range(n):
                if not used[i]:
                    used[i] = True
                    dfs(path + [nums[i]])
                    used[i] = False

        dfs([])

        return res
