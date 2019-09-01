#!/usr/bin/env python3

from typing import List


class Solution:

    def oddEvenJumps(self, A: List[int]) -> int:

        def mono_stack(index_list: List[int]):
            next_arr = [None for _ in range(n)]
            stack = []
            for i in index_list:
                while stack and stack[-1] < i:
                    next_arr[stack.pop()] = i
                stack.append(i)

            return next_arr

        n = len(A)

        if n == 0:
            return 0

        if n == 1:
            return 1

        index_list = sorted(range(n), key=lambda i: A[i])
        next_large = mono_stack(index_list)
        index_list.sort(key=lambda i: A[i], reverse=True)
        next_small = mono_stack(index_list)

        dp = [[False, False] for _ in range(n)]

        dp[n - 1][0], dp[n - 1][1] = True, True

        for i in range(n - 2, -1, -1):
            if next_large[i]:
                dp[i][0] = dp[next_large[i]][1]

            if next_small[i]:
                dp[i][1] = dp[next_small[i]][0]

        res = 0
        for i in range(n):
            if dp[i][0]:
                res += 1
        return res
