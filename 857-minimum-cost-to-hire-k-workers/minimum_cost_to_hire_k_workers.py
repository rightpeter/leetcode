#!/usr/bin/env python3

from typing import List
import heapq


class Solution:

    def mincostToHireWorkers(self, quality: List[int], wage: List[int],
                             K: int) -> float:
        n = len(quality)

        workers = [i for i in range(n)]

        workers.sort(key=lambda i: wage[i] / quality[i])

        pq = []
        sum_quality = 0
        for i in workers[:K]:
            heapq.heappush(pq, [-quality[i], i])
            sum_quality += quality[i]
        res = sum_quality * wage[workers[K - 1]] / quality[workers[K - 1]]

        for i in workers[K:]:
            _, j = heapq.heappop(pq)
            heapq.heappush(pq, [-quality[i], i])
            sum_quality -= quality[j]
            sum_quality += quality[i]

            res = min(res, sum_quality * wage[i] / quality[i])

        return res
