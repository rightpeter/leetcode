#!/usr/bin/env python3

factorial_map = {
    0: 1,
    1: 1,
    2: 2,
    3: 6,
    4: 24,
    5: 120,
    6: 720,
    7: 5040,
    8: 40320,
}


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        elements = [i for i in range(1, n + 1)]

        k -= 1

        res = ''
        for i in range(n, 0, -1):
            e = k // factorial_map[i - 1]
            res += str(elements[e])
            elements = elements[:e] + elements[e + 1:]
            k = k % factorial_map[i - 1]

        return res
