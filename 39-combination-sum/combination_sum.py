#!/usr/bin/env python3

from typing import List


class Solution:
    def find(self, target, l: int) -> List[List[List[int]]]:
        if l in self.cache and target in self.cache[l]:
            return self.cache[l][target]

        if l >= len(self.candidates):
            return []

        res = []
        for i in range(int(target / self.candidates[l]) + 1):
            if target == i * self.candidates[l]:
                res.append([[self.candidates[l], i]])
            else:
                combs = self.find(target - i * self.candidates[l], l + 1)
                res += [[[self.candidates[l], i]] + comb for comb in combs]

        if l not in self.cache:
            self.cache[l] = {}

        self.cache[l][target] = res
        return res

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.cache = {}
        self.candidates = candidates
        res_combs = self.find(target, 0)

        res = []

        for comb in res_combs:
            tmp_comb = []

            for candidate in comb:
                if candidate[1] != 0:
                    for _ in range(candidate[1]):
                        tmp_comb.append(candidate[0])

            res.append(tmp_comb)

        return res
