#!/usr/bin/env python3

from typing import List


class Solution:

    def grayCode(self, n: int) -> List[int]:

        def dfs(n: int):
            if n == 0:
                return [0]

            suffix = dfs(n - 1)
            return suffix + [x + 2**(n - 1) for x in reversed(suffix)]

        return dfs(n)
