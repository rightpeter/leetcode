#!/usr/bin/env python3

from typing import List
import itertools as it


class Solution:

    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        res = 0
        n = len(grid)
        if n == 0:
            return 0

        m = len(grid[0])
        if m == 0:
            return 0

        for r1, r2 in it.combinations(grid, 2):
            tmp = 0
            for i in range(m):
                if r1[i] == r2[i] == 1:
                    tmp += 1
            res += tmp * (tmp - 1) / 2

        return int(res)
