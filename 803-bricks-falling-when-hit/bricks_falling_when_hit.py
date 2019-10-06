#!/usr/bin/env python3

from typing import List

directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
SOLIC_BRICK = 2


class Solution:

    def hitBricks(self, grid: List[List[int]],
                  hits: List[List[int]]) -> List[int]:
        n = len(grid)
        m = len(grid[0])

        if not len(hits):
            return []

        for x, y in hits:
            grid[x][y] *= -1

        def is_top(x: int) -> bool:
            return x == -1

        def is_solic_brick(x: int, y: int) -> bool:
            if not in_grid(x, y):
                return False

            return grid[x][y] == SOLIC_BRICK

        def in_grid(x: int, y: int) -> bool:
            if 0 <= x < n and 0 <= y < m:
                return True

            return False

        def is_save(hit: List[int]) -> bool:
            for i in range(4):
                x = hit[0] + directions[i][0]
                y = hit[1] + directions[i][1]
                if is_top(x) or is_solic_brick(x, y):
                    return True

            return False

        def coloring(start: List[int]) -> int:
            if grid[start[0]][start[1]] != 1:
                return 0

            count = 1
            grid[start[0]][start[1]] = SOLIC_BRICK
            queue = [start]

            while queue:
                brick = queue.pop(0)
                for i in range(4):
                    x = brick[0] + directions[i][0]
                    y = brick[1] + directions[i][1]
                    if in_grid(x, y) and grid[x][y] == 1:
                        grid[x][y] = SOLIC_BRICK
                        count += 1
                        queue.append([x, y])

            return count

        for j in range(m):
            coloring([0, j])

        res = []
        hits.reverse()
        for hit in hits:
            if grid[hit[0]][hit[1]] == 0:
                res.append(0)
            else:
                grid[hit[0]][hit[1]] = 1
                if is_save(hit):
                    res.append(max(coloring(hit) - 1, 0))
                else:
                    res.append(0)

        res.reverse()
        return res
