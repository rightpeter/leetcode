#!/usr/bin/env python3

ROMAN_TO_DIGIT = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1,
}


class Solution:

    def romanToInt(self, s: str) -> int:
        p = 2000
        x = 0
        res = 0
        for c in s:
            x = ROMAN_TO_DIGIT[c]

            if p >= x:
                res += x
            else:
                res -= 2 * p
                res += x

            p = x

        return res
