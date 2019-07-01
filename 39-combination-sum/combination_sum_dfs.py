#!/usr/bin/env python3

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(target, index: int, comb: List[int]):
            if target == 0:
                res.append(comb)

            for i in range(index, len(candidates)):
                if target - candidates[i] >= 0:
                    dfs(target - candidates[i], i, comb + [candidates[i]])
                else:
                    break

        res = []

        candidates.sort()
        dfs(target, 0, [])

        return res
