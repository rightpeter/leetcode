#!/usr/bin/env python3


class Solution:

    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums = sorted(nums)
        nums_sum = sum(nums)

        n = len(nums)

        if nums_sum % 2 != 0:
            return False

        target = nums_sum / 2

        dp = set([0, nums[0]])
        if target in dp:
            return True

        for i in range(1, n):
            dp_new = dp.copy()

            for num in dp:
                if num + nums[i] == target:
                    return True

                dp_new.add(num + nums[i])

            dp = dp_new

        return False
