#!/usr/bin/env python3

from typing import List
from collections import defaultdict


class Solution:

    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)

        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        sum_dis = [0] * N
        child_nums = [0] * N

        def cal_children(node: int, parent: int):
            for child in graph[node]:
                if child == parent:
                    continue

                cal_children(child, node)
                sum_dis[node] += sum_dis[child] + child_nums[child] + 1
                child_nums[node] += child_nums[child] + 1

        def cal_parents(node: int, parent: int, sum_parent: int,
                        num_parent: int):
            sum_dis[node] += sum_parent + num_parent
            for child in graph[node]:
                if child == parent:
                    continue

                num_child = num_parent + child_nums[node] - child_nums[child]
                sum_child = sum_dis[node] - sum_dis[child] - child_nums[
                    child] - 1
                cal_parents(child, node, sum_child, num_child)

        cal_children(0, 0)

        cal_parents(0, 0, 0, 0)

        return sum_dis
