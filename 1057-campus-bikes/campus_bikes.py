#!/usr/bin/env python3

from typing import List


class Solution:

    def assignBikes(self, workers: List[List[int]],
                    bikes: List[List[int]]) -> List[int]:

        def distance(worker, bike):
            return abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])

        n = len(workers)
        m = len(bikes)

        if n == 0:
            return []

        pairs = []
        for i in range(n):
            for j in range(m):
                pairs.append([distance(workers[i], bikes[j]), i, j])

        pairs.sort(key=lambda x: x[0])

        bikes_set = set()
        res = [-1] * n

        for pair in pairs:
            if res[pair[1]] == -1 and pair[2] not in bikes_set:
                res[pair[1]] = pair[2]
                bikes_set.add(pair[2])

        return res
