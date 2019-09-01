#!/usr/bin/env python3

from typing import List
from collections import deque


class Solution:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        def clean_queue(i: int):
            if queue and queue[0] == i - k:
                queue.popleft()

            while queue and nums[queue[-1]] <= nums[i]:
                queue.pop()

        n = len(nums)
        if n == 0:
            return []

        queue = deque()
        for i in range(k):
            clean_queue(i)
            queue.append(i)

        res = [nums[queue[0]]]

        for i in range(k, n):
            clean_queue(i)
            queue.append(i)

            res.append(nums[queue[0]])

        return res
