#!/usr/bin/env python3

from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        i = 0
        d = 0
        while seats[i] == 0:
            d += 1
            i += 1

        j = len(seats) - 1
        td = 0
        while seats[j] == 0:
            j -= 1
            td += 1

        d = max(d, td)

        while i <= j:
            i += 1
            td = 0
            while i <= j and seats[i] == 0:
                i += 1
                td += 1
            d = max(d, (td + 1) // 2)

        return d
