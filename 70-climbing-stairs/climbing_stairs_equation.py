#!/usr/bin/env python3


class Solution:
    def climbStairs(self, n: int) -> int:
        factorial_map = [1 for _ in range(n)]

        for i in range(1, n):
            factorial_map[i] = factorial_map[i - 1] * i

        # for i in range(n):
            # print(f'{i}: {factorial_map[i]}')

        res = 1
        for i in range(1, n // 2 + 1):
            res += factorial_map[n - i] // (factorial_map[n - 2 * i] * factorial_map[i])

        return res
