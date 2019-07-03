#!/usr/bin/env python3


class Solution:
    def myPow(self, x: float, n: int) -> float:
        cache = {}

        def helper_pow(x: float, n: int) -> float:
            if n == 0:
                return 1

            if x in cache and n in cache[x]:
                return cache[x][n]

            if n % 2 == 0:
                return helper_pow(x, n / 2)**2
            else:
                return helper_pow(x, (n - 1) / 2)**2 * x

        if n == 0:
            return 1

        if n < 0:
            n = -n
            x = 1 / x

        return helper_pow(x, n)
