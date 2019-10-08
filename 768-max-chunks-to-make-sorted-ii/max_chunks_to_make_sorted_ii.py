#!/usr/bin/env python3

from typing import List


class Solution:

    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        after_min = [0] * n
        before_max = [0] * n

        tmax = arr[0]
        tmin = arr[-1]
        for i in range(n):
            j = n - 1 - i
            tmax = max(tmax, arr[i])
            tmin = min(tmin, arr[j])
            before_max[i] = tmax
            after_min[j] = tmin

        res = 0
        for i in range(n - 1):
            if before_max[i] <= after_min[i + 1]:
                res += 1

        return res + 1
