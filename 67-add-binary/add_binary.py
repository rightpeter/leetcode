#!/usr/bin/env python3

from typing import Tuple


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def add_bit(a: int, b: int, c: int) -> Tuple[int, str]:
            return (a + b + c) // 2, str((a + b + c) % 2)

        if len(b) > len(a):
            a, b = b, a
        n, m = len(a), len(b)

        if n == 0 or m == 0:
            return ''

        res = list(a)

        i = 1
        carry = 0
        while i <= m:
            carry, res[-i] = add_bit(int(a[-i]), int(b[-i]), carry)
            i += 1

        while i <= n and carry > 0:
            carry, res[-i] = add_bit(int(a[-i]), 0, carry)
            i += 1

        res = ''.join(res)
        if carry > 0:
            res = '1' + res

        return res
