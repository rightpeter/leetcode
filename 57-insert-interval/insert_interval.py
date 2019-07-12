#!/usr/bin/env python3

from typing import List, Tuple


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def bin_search(target: int) -> Tuple[int, bool]:
            l = 0
            r = len(intervals) - 1

            while l <= r:
                p = int((l + r) / 2)

                if intervals[p][0] <= target <= intervals[p][1]:
                    return p, True
                elif intervals[p][0] > target:
                    r = p - 1
                else:
                    l = p + 1

            return l, False

        left, found = bin_search(newInterval[0])
        left_intervals = intervals[:left]
        if found:
            lower_bound = intervals[left][0]
        else:
            lower_bound = newInterval[0]

        right, found = bin_search(newInterval[1])
        if found:
            right_intervals = intervals[right + 1:]
            upper_bound = intervals[right][1]
        else:
            right_intervals = intervals[right:]
            upper_bound = newInterval[1]

        return left_intervals + [[lower_bound, upper_bound]] + right_intervals
