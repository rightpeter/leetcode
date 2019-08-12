#!/usr/bin/env python3

from typing import List


class Solution:

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        hi = m + n - 1
        i = m - 1
        j = n - 1

        for _ in range(m + n):
            if i >= 0 and (j < 0 or nums1[i] >= nums2[j]):
                nums1[hi] = nums1[i]
                i -= 1
            else:
                nums1[hi] = nums2[j]
                j -= 1
            hi -= 1
