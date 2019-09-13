#!/usr/bin/env python3

# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]


class Solution:

    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """

        def anti_clock(d):
            robot.turnLeft()
            return (d - 1) % 4

        def clock_wise(d):
            robot.turnRight()
            return (d + 1) % 4

        def turn_180(d):
            robot.turnRight()
            robot.turnRight()
            return (d + 2) % 4

        visited = []

        def dfs(x, y, d: int):
            # print(f'({x}, {y}), d: {d}')
            robot.clean()
            visited.append((x, y))

            for _ in range(3):
                d = anti_clock(d)
                nx = x + directions[d][0]
                ny = y + directions[d][1]

                if (nx, ny) in visited:
                    # print(f'visited ({nx}, {ny}), d: {d}')
                    d = turn_180(d)
                    continue

                if robot.move():
                    d = dfs(nx, ny, d)
                    robot.move()
                else:
                    # print(f'wall ({nx}, {ny}), d: {d}')
                    visited.append((nx, ny))
                    d = turn_180(d)

            return anti_clock(d)

        print('------------------------ dfs(0, 0, 0) ------------------------')
        dfs(0, 0, 0)
        robot.move()
        print('------------------------ dfs(1, 0, 2) ------------------------')
        dfs(1, 0, 2)
