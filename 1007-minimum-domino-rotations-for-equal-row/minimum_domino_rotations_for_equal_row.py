#!/usr/bin/env python3

from typing import List


class Solution:

    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        n = len(A)

        if n <= 1:
            return 0

        can_dict = {}
        if A[0] == B[0]:
            can_dict[A[0]] = [0, 0]
        else:
            can_dict[A[0]] = [0, 1]
            can_dict[B[0]] = [1, 0]

        for i in range(1, n):
            if A[0] not in [A[i], B[i]] and A[0] in can_dict:
                del (can_dict[A[0]])

            if B[0] not in [A[i], B[i]] and B[0] in can_dict:
                del (can_dict[B[0]])

            if not can_dict:
                return -1

            if A[i] == B[i]:
                continue

            if A[i] in can_dict:
                can_dict[A[i]][1] += 1

            if B[i] in can_dict:
                can_dict[B[i]][0] += 1

        res = float('inf')

        if A[0] in can_dict:
            res = min(res, min(can_dict[A[0]]))

        if B[0] in can_dict:
            res = min(res, min(can_dict[B[0]]))

        return res
