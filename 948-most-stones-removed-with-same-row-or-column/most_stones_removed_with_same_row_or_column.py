#!/usr/bin/env python3

from typing import List
from collections import defaultdict


class Solution:

    def removeStones(self, stones: List[List[int]]) -> int:

        def find_components(stone: List[int]):
            nonlocal seen
            nonlocal row_stones
            nonlocal col_stones

            queue = [stone]
            while queue:
                x, y = queue.pop(0)
                if (x, y) in seen:
                    continue

                seen.add((x, y))
                for yy in row_stones[x]:
                    find_components([x, yy])

                for xx in col_stones[y]:
                    find_components([xx, y])

        components = 0
        seen = set()

        row_stones = defaultdict(set)
        col_stones = defaultdict(set)

        for stone in stones:
            row_stones[stone[0]].add(stone[1])
            col_stones[stone[1]].add(stone[0])

        for stone in stones:
            if tuple(stone) not in seen:
                components += 1
                find_components(stone)

        return len(stones) - components
