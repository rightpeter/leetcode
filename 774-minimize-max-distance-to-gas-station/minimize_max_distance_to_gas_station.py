#!/usr/bin/env python3

from typing import List


class Solution:

    def minmaxGasDist(self, stations: List[int], K: int) -> float:
        dp = [0 for _ in range(K + 1)]
        d = [stations[i + 1] - stations[i] for i in range(0, len(stations) - 1)]

        for i in range(1, len(stations)):
            for k in range(K, -1, -1):
                dp[k] = min([
                    max(dp[k - j], (d[i - 1]) / (j + 1))
                    for j in range(0, k + 1)
                ])

        return dp[K]
