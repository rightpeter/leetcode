#!/usr/bin/env python3

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        if n == 0:
            return 0

        def find(l, r: int):
            min_i = l

            if r <= l:
                # print(f'l: {l}, r: {r}, return 0')
                return 0

            if r == l + 1:
                # print(f'l: {l}, r: {r}, return {heights[l]}')
                return heights[l]

            for i in range(l, r):
                if heights[i] < heights[min_i]:
                    min_i = i

            # print(
                # f'l: {l}, min_i: {min_i}, r: {r}, {heights[min_i]*(r-l)}, find({l}, {i}): {find(l, i)}, find({i+1}, {r}); {find(i+1, r)}'
            # )
            return max(heights[min_i] * (r - l), find(l, min_i), find(min_i + 1, r))

        return find(0, len(heights))
