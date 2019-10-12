#!/usr/bin/env python3

from typing import List


class Solution:

    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = [0]
        res = [0] * len(T)
        for j in range(1, len(T)):
            t = T[j]
            while stack and T[stack[-1]] < t:
                i = stack.pop(-1)
                res[i] = j - i

            stack.append(j)

        return res
