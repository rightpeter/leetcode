#!/usr/bin/env python3

from typing import List


class Solution:

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def find_root(i: int) -> int:
            while union_find[i] != i:
                i = union_find[i]

            return i

        n = len(edges)
        if n == 0:
            return []

        if n == 1:
            return edges[0]

        union_find = [i for i in range(n + 1)]

        for edge in edges:
            if find_root(edge[0]) == find_root(edge[1]):
                return edge

            union_find[find_root(edge[1])] = union_find[find_root(edge[0])]
