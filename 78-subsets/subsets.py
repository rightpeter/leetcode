#!/usr/bin/env python3

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(step: int, path: List[int]):
            if step >= len(nums):
                res.append(path.copy())
                return

            dfs(step + 1, path)

            path.append(nums[step])
            dfs(step + 1, path)
            del (path[-1])

        dfs(0, [])

        return res
