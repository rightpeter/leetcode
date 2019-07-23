#!/usr/bin/env python3

from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 0:
            return []

        def dfs(l: int, step: int, path: List[int]):
            nonlocal res
            if step > k:
                res.append(path.copy())
                return

            for i in range(l, n + 1):
                path.append(i)
                dfs(i + 1, step + 1, path)
                del(path[-1])

        res = []

        dfs(1, 1, [])
        return res
