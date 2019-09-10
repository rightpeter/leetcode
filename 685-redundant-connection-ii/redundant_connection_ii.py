#!/usr/bin/env python3

from typing import List


class Solution:

    def findRedundantDirectedConnection(self,
                                        edges: List[List[int]]) -> List[int]:
        n = len(edges)
        if n == 0:
            return []

        if n == 1:
            return edges[0]

        parent = [-1] * (n + 1)
        edge_candidates = []

        for u, v in edges:
            if parent[v] != -1:
                edge_candidates.append([parent[v], v])
                edge_candidates.append([u, v])
            else:
                parent[v] = u

        def find_root(i: int) -> int:
            seen = []
            while parent[i] != -1 and i not in seen:
                seen.append(i)
                i = parent[i]

            return i, seen

        if not edge_candidates:
            circle = find_root(1)[1]

            ans = []
            for u, v in edges:
                if u in circle and v in circle:
                    ans = [u, v]

            return ans
        else:
            edge = edge_candidates[0]
            root, seen = find_root(edge[1])
            if root in seen:
                return edge

            edge = edge_candidates[1]
            parent[edge[1]] = edge[0]
            root, seen = find_root(edge[1])
            if root in seen:
                return edge

            return edge
