#!/usr/bin/env python3

from typing import List
from random import randint


class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = []
        self.s_sum = []
        tot = 0
        for rect in rects:
            w = rect[2] - rect[0] + 1
            h = rect[3] - rect[1] + 1
            self.rects.append([rect[0], rect[1], w, h])
            tot += w * h
            self.s_sum.append(tot)

    def find_rect(self, r: int) -> int:
        lo = 0
        hi = len(self.s_sum) - 1
        while lo <= hi:
            mid = (lo + hi) // 2

            if self.s_sum[mid] < r:
                lo = mid + 1
                continue

            if mid != 0 and r <= self.s_sum[mid - 1]:
                hi = mid - 1
                continue

            return mid

    def pick(self) -> List[int]:
        print(f's_sum: {self.s_sum[-1]}')
        r = randint(1, self.s_sum[-1])
        print(f'r: {r}')
        index = self.find_rect(r)
        print(f'index: {index}')
        rect = self.rects[index]
        print(f'rect: {rect}')
        s = r - self.s_sum[index - 1] if index > 0 else r
        print(f's: {s}')
        xx = (s - 1) % rect[2]
        yy = (s - 1) // rect[2]
        print(f'(xx, yy): {(xx, yy)}')
        return [rect[0] + xx, rect[1] + yy]


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
