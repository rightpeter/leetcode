#!/usr/bin/env python3

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        if n == 0:
            return False

        m = len(matrix[0])
        if m == 0:
            return False

        l = 0
        r = n - 1

        while l <= r:
            p = (l + r) // 2
            if matrix[p][0] == target:
                return True
            elif matrix[p][0] < target:
                l = p + 1
            else:
                r = p - 1

        i = r

        if i < 0 or i >= n:
            return False

        l = 0
        r = m - 1

        while l <= r:
            p = (l + r) // 2
            if matrix[i][p] == target:
                return True
            elif matrix[i][p] < target:
                l = p + 1
            else:
                r = p - 1

        return False
