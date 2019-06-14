#!/usr/bin/env python3


class Solution:

    def divide(self, dividend: int, divisor: int) -> int:
        count = 0
        pref = 1

        if dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0:
            pref = -1

        dividend = abs(dividend)
        divisor = abs(divisor)

        divisors = []

        latest_divisor = divisor
        mul = 1
        while latest_divisor <= dividend:
            divisors.append([latest_divisor, mul])
            latest_divisor += latest_divisor
            mul += mul

        res = 0
        for divisor, mul in reversed(divisors):
            if dividend >= divisor:
                dividend -= divisor
                res += mul

        return min(pref * res, 2147483647)
