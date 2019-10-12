#!/usr/bin/env python3

import bisect


class MyCalendarTwo:

    def __init__(self):
        self.time_map = {}
        self.sorted_date = []

    def book(self, start: int, end: int) -> bool:

        if start not in self.time_map:
            self.time_map[start] = [start, 1, 0]
            bisect.insort(self.sorted_date, self.time_map[start])
        else:
            self.time_map[start][1] += 1

        if end not in self.time_map:
            self.time_map[end] = [end, 0, 1]
            bisect.insort(self.sorted_date, self.time_map[end])
        else:
            self.time_map[end][2] += 1

        events = 0

        for date, s, e in self.sorted_date:
            events -= e
            events += s

            if events >= 3:
                self.time_map[start][1] -= 1
                self.time_map[end][2] -= 1

                return False

        return True
