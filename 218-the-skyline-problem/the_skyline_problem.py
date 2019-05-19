#!/usr/bin/env python3


class Solution:

    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """

        points = []
        for building in buildings:
            # [l, r, h]
            points.append([building[0], building[2], False])
            points.append([building[1], building[2], True])

        points = sorted(points, key=lambda p: p[0])

        ans = []
        heights = [0]
        previous_max = 0
        i = 0
        print(points)
        while i < len(points):
            if points[i][2]:
                heights.remove(points[i][1])
            else:
                heights.append(points[i][1])

            while i + 1 < len(points) and points[i + 1][0] == points[i][0]:
                i += 1

                if points[i][2]:
                    heights.remove(points[i][1])
                else:
                    heights.append(points[i][1])

            heights = sorted(heights, reverse=True)

            if heights[0] != previous_max:
                ans.append([points[i][0], heights[0]])
                previous_max = heights[0]

            i += 1

        return ans
