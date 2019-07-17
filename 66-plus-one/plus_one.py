#!/usr/bin/env python3

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        if n == 0:
            return []

        residual = (digits[-1] + 1) // 10
        digits[-1] = (digits[-1] + 1) % 10

        i = n - 2
        while residual > 0 and i >= 0:
            residual = (digits[i] + 1) // 10
            digits[i] = (digits[i] + 1) % 10
            i -= 1

        if residual > 0:
            digits = [residual] + digits
        return digits
