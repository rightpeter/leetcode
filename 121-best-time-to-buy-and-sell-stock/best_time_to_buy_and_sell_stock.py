#!/usr/bin/env python3

from typing import List


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        prev_min = prices[0]
        res = 0

        for price in prices:
            res = max(res, price - prev_min)
            prev_min = min(prev_min, price)

        return res
