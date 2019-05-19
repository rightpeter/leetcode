#!/usr/bin/env python3


class Solution:

    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count_map = {}
        for num in nums:
            if num in count_map:
                count_map[num] += 1
            else:
                count_map[num] = 1

        return sorted(count_map, key=lambda k: count_map[k], reverse=True)[:k]
