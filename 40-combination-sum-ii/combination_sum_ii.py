#!/usr/bin/env python3

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(target, index: int, comb: List[int]):
            if target < 0:
                return

            # print(f'target: {target}, index: {index}, comb: {comb}')

            if index >= len(candidates):
                return

            r = index + 1
            count = 1
            while r < len(candidates) and candidates[r] == candidates[index]:
                count += 1
                r += 1

            for i in range(count + 1):
                if target == candidates[index] * i:
                    res.append(comb + [candidates[index]] * i)
                    return
                elif target > candidates[index] * i:
                    # print(f'c: {i}')
                    dfs(target - candidates[index] * i, r, comb + [candidates[index]] * i)

        res = []

        candidates.sort()
        # print(f'candidates: {candidates}')
        dfs(target, 0, [])

        return res
