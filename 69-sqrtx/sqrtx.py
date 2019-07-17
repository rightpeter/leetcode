#!/usr/bin/env python3


class Solution:
    def mySqrt(self, x: int) -> int:
        if x in {1, 2, 3}:
            return 1

        l = 1
        r = x // 2

        while l <= r:
            p = (l + r) // 2
            if p * p == x:
                return p
            elif p * p > x:
                r = p - 1
            else:
                l = p + 1

        return r
