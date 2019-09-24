#!/usr/bin/env python3

from typing import List


class Solution:

    def carFleet(self, target: int, position: List[int],
                 speed: List[int]) -> int:
        n = len(position)
        if n == 0:
            return 0

        cars = [i for i in range(n)]
        cars.sort(key=lambda i: -position[i])

        fleets = []

        for car in cars:
            time = (target - position[car]) / speed[car]
            if not fleets:
                fleets.append(time)
            else:
                if time > fleets[-1]:
                    fleets.append(time)

        return len(fleets)
