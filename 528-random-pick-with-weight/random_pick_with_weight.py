#!/usr/bin/env python3

from typing import List
import random


class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.sum_w = w
        for i in range(1, len(self.sum_w)):
            self.sum_w[i] += self.sum_w[i - 1]
        self.max_w = self.sum_w[-1]

    def findWeight(self, r: int):
        i = 0
        j = len(self.sum_w) - 1

        while i <= j:
            mid = (i + j) // 2
            if self.sum_w[mid] < r:
                i = mid + 1
                continue

            if mid > 0 and r <= self.sum_w[mid - 1]:
                j = mid - 1
                continue

            return mid

    def pickIndex(self) -> int:
        return self.findWeight(random.randint(1, self.max_w))


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
