#!/usr/bin/env python3

from typing import List
from collections import defaultdict


class Solution:

    def calcEquation(self, equations: List[List[str]], values: List[float],
                     queries: List[List[str]]) -> List[float]:
        edges = defaultdict(list)
        memo = defaultdict(dict)

        for i, equation in enumerate(equations):
            u, v = equation[0], equation[1]
            edges[u].append([v, values[i]])
            edges[v].append([u, 1 / values[i]])

        def dfs(start: str, target: str, seen: set) -> float:
            if target in memo[start]:
                return memo[start][target]

            if edges[start] and start == target:
                memo[start][target] = 1.0
                return memo[start][target]

            seen.add(start)
            for v, cvalue in edges[start]:
                if v in seen:
                    continue

                value = dfs(v, target, seen)
                if value > 0:
                    memo[start][target] = cvalue * value
                    return memo[start][target]

            return -1

        res = []
        for u, v in queries:
            res.append(dfs(u, v, set()))

        return res
