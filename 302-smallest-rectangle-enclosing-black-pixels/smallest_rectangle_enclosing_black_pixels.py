#!/usr/bin/env python3

from typing import List


class Solution:

    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        n = len(image)
        if not n:
            return 0

        m = len(image[0])
        if not m:
            return 0

        def search(lo: int, hi: int, direction: int, axis: int) -> int:
            lo *= direction
            hi *= direction

            while lo <= hi:
                mid = (lo + hi) // 2

                has_black = False
                i = 0
                if axis == 0:
                    while i < m and image[direction * mid][i] == '0':
                        i += 1
                    if i < m:
                        has_black = True
                else:
                    while i < n and image[i][direction * mid] == '0':
                        i += 1
                    if i < n:
                        has_black = True

                if has_black:
                    lo = mid + 1
                else:
                    hi = mid - 1

            return hi * direction

        x1 = search(x, 0, -1, 0)
        x2 = search(x, n - 1, 1, 0)

        y1 = search(y, 0, -1, 1)
        y2 = search(y, m - 1, 1, 1)

        return (x2 - x1 + 1) * (y2 - y1 + 1)
