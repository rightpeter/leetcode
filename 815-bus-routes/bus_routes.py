#!/usr/bin/env python3

from typing import List
import collections


class Solution:

    def numBusesToDestination(self, routes: List[List[int]], S: int,
                              T: int) -> int:
        n = len(routes)
        if n == 0:
            return -1

        if S == T:
            return 0

        routes = [set(route) for route in routes]
        stop_to_route = collections.defaultdict(set)
        seen_routes = set()

        for i, route in enumerate(routes):
            for stop in route:
                stop_to_route[stop].add(i)

        queue = [(i, 1) for i in stop_to_route[S]]
        seen_routes.update(stop_to_route[S])

        while queue:
            i, step = queue.pop(0)

            for stop in routes[i]:
                if stop == T:
                    return step

                for j in stop_to_route[stop]:
                    if j not in seen_routes:
                        queue.append((j, step + 1))
                        seen_routes.add(j)

        return -1
