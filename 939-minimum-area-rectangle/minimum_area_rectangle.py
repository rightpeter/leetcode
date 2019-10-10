#!/usr/bin/env python3

from typing import List
from collections import defaultdict
from itertools import combinations


class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:
        points_map = defaultdict(set)
        for x, y in points:
            points_map[x].add(y)

        xs = sorted(points_map)

        res = float('inf')
        for x1, x2 in combinations(xs, 2):
            ys = sorted(points_map[x1].intersection(points_map[x2]))
            if len(ys) > 1:
                min_width = min([ys[i] - ys[i - 1] for i in range(1, len(ys))])
                res = min(res, abs(x2 - x1) * min_width)

        return res if res < float('inf') else 0
