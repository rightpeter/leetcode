#!/usr/bin/env python3

from typing import List


class Solution:

    def kEmptySlots(self, bulbs: List[int], K: int) -> int:
        n = len(bulbs)
        days = [0] * n

        for day, bulb in enumerate(bulbs):
            days[bulb - 1] = day + 1

        res = float('inf')

        lo, hi = 0, K + 1
        while hi < n:
            for i in range(lo + 1, hi):
                if days[i] <= days[lo] or days[i] <= days[hi]:
                    lo, hi = i, i + K + 1
                    break
            else:
                res = min(res, max(days[lo], days[hi]))
                lo, hi = hi, hi + K + 1

        return res if res < float('inf') else -1
