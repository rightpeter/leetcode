#!/usr/bin/env python3

from typing import List


class Solution:

    def minmaxGasDist(self, stations: List[int], K: int) -> float:
        d = [stations[i + 1] - stations[i] for i in range(len(stations) - 1)]

        def valid(D: int) -> bool:
            return sum(int(dis / D) for dis in d) <= K

        lo = 0
        hi = max(d)

        while hi - lo > 1e-6:
            mid = (lo + hi) / 2
            if valid(mid):
                hi = mid
            else:
                lo = mid

        return (hi + lo) / 2
