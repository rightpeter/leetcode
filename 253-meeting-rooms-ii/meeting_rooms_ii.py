#!/usr/bin/env python3

from typing import List


class Solution:

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        events = []
        for interval in intervals:
            events.append([interval[0], 0])
            events.append([interval[1], 1])

        events.sort(key=lambda x: x[1], reverse=True)
        events.sort(key=lambda x: x[0])

        res = 0
        tmp = 0

        for e in events:
            if e[1] == 0:
                tmp += 1
                res = max(tmp, res)
            else:
                tmp -= 1

        return res
