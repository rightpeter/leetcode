#!/usr/bin/env python3

from typing import List


class Solution:

    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums.append(1)
        max_coins = [[-1] * n for _ in range(n)]

        def find_max_coins(lo: int, hi: int) -> int:
            if hi < lo:
                return 0

            if max_coins[lo][hi] > -1:
                return max_coins[lo][hi]

            if lo == hi:
                max_coins[lo][hi] = nums[lo - 1] * nums[lo] * nums[hi + 1]
            else:
                max_coins[lo][hi] = max(
                    find_max_coins(lo, i - 1) +
                    nums[lo - 1] * nums[i] * nums[hi + 1] +
                    find_max_coins(i + 1, hi) for i in range(lo, hi + 1))

            return max_coins[lo][hi]

        return find_max_coins(0, n - 1)
