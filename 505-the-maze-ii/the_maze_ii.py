#!/usr/bin/env python3

from typing import List

DIRECTIONS = [[-1, 0], [0, 1], [1, 0], [0, -1]]


class Solution:

    def shortestDistance(self, maze: List[List[int]], start: List[int],
                         destination: List[int]) -> int:

        def is_wall(x: int, y: int) -> bool:
            return x < 0 or x >= n or y < 0 or y >= m or maze[x][y] == 1

        n = len(maze)
        if not n:
            return -1

        m = len(maze[0])
        if not m:
            return -1

        queue = [start]
        maze[start[0]][start[1]] = -1
        while queue:
            curr = queue.pop(0)

            for direction in range(4):
                x, y = curr
                count = 0
                nx = x + DIRECTIONS[direction][0]
                ny = y + DIRECTIONS[direction][1]

                while not is_wall(nx, ny):
                    x, y = nx, ny
                    nx = x + DIRECTIONS[direction][0]
                    ny = y + DIRECTIONS[direction][1]
                    count += 1

                if maze[x][
                        y] == 0 or maze[x][y] < maze[curr[0]][curr[1]] - count:
                    queue.append([x, y])
                    maze[x][y] = maze[curr[0]][curr[1]] - count

        return -1 if maze[destination[0]][destination[1]] == 0 else (
            -maze[destination[0]][destination[1]] - 1)
