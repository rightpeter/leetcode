#!/usr/bin/env python3

from typing import List


class Solution:

    def maxChunksToSorted(self, arr: List[int]) -> int:
        def add_remove_num(num: int):
            nonlocal nums
            nonlocal count

            if nums[num]:
                nums[num] = 0
                count -= 1
            else:
                nums[num] = 1
                count += 1

        i = 0
        res = 0
        nums = [0] * len(arr)
        count = 0

        while i < len(arr):
            add_remove_num(i)
            add_remove_num(arr[i])
            if not count:
                res += 1

            i += 1

        return res
