#!/usr/bin/env python3

from typing import List


class Solution:

    def isPossible(self, nums: List[int]) -> bool:
        n = len(nums)

        counts = []
        i = 0
        while i < n:
            j = i
            while j < n and nums[j] == nums[i]:
                j += 1

            count = j - i

            if i > 0 and nums[i] != nums[i - 1] + 1:
                for c in counts:
                    if c < 3:
                        return False

                counts = [1 for _ in range(count)]
            else:
                if not counts:
                    counts = [1 for _ in range(count)]
                else:
                    if count >= len(counts):
                        counts = [1 for _ in range(count - len(counts))] + [c + 1 for c in counts]
                    else:
                        for _ in range(len(counts) - count):
                            if counts.pop(-1) < 3:
                                return False

                        counts = [c + 1 for c in counts]

            i = j

        while counts:
            if counts.pop(-1) < 3:
                return False

        return True
