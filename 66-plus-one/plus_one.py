#!/usr/bin/env python3

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        if n == 0:
            return []

        carry = (digits[-1] + 1) // 10
        digits[-1] = (digits[-1] + 1) % 10

        i = n - 2
        while carry > 0 and i >= 0:
            carry = (digits[i] + 1) // 10
            digits[i] = (digits[i] + 1) % 10
            i -= 1

        if carry > 0:
            digits = [carry] + digits
        return digits
