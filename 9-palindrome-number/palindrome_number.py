#!/usr/bin/env python3


class Solution:

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True

        t = x
        xx = 0

        while t > 0:
            a = t % 10
            t = t // 10
            xx = 10 * xx + a

        return x == xx
