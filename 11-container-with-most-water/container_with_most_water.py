#!/usr/bin/env python3

from typing import List


class Solution:

    def maxArea(self, height: List[int]) -> int:
        max_S = 0
        n = len(height)

        i = 0
        j = n - 1

        while i < j:
            max_S = max(max_S, min(height[i], height[j]) * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return max_S
