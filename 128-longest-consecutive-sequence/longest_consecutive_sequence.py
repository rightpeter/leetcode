#!/usr/bin/env python3


class Solution:

    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)

        ans = 0
        streak = 0
        for num in nums:
            if num - 1 not in nums:
                streak = 1
                tmp = num
                while tmp + 1 in nums:
                    tmp += 1
                    streak += 1
                ans = max(streak, ans)

        return ans
