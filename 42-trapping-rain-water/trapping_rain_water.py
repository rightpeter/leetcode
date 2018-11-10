#!/usr/bin/env python3


class Solution:

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        n = len(height)
        if n == 0:
            return 0
        # print("n: ", n)
        min_height = min(height)

        dp_left = [min_height for i in height]
        dp_right = [min_height for i in height]
        dp_left[0] = height[0]
        for i in range(1, n):
            dp_left[i] = max(dp_left[i - 1], height[i])

        dp_right[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            dp_right[i] = max(dp_right[i + 1], height[i])

        ans = 0
        for i in range(n):
            min_max = min(dp_left[i], dp_right[i])
            ans += min_max - height[i]
        return ans
