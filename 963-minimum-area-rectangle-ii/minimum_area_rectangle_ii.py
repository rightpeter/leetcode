#!/usr/bin/env python3

from typing import List
from itertools import permutations
import math


class Solution:

    def minAreaFreeRect(self, points: List[List[int]]) -> float:

        points = set(map(tuple, points))

        res = float('inf')
        for p1, p2, p3 in permutations(points, 3):
            e1 = (p2[0] - p1[0], p2[1] - p1[1])
            e2 = (p3[0] - p1[0], p3[1] - p1[1])

            p4 = (p2[0] + p3[0] - p1[0], p2[1] + p3[1] - p1[1])

            if p4 not in points:
                continue

            if e1[0] * e2[0] + e1[1] * e2[1] != 0:
                continue

            ae1 = math.sqrt((e1[0])**2 + (e1[1])**2)
            ae2 = math.sqrt((e2[0])**2 + (e2[1])**2)

            s = ae1 * ae2
            if s >= res:
                continue

            res = s

        return 0 if res == float('inf') else res
