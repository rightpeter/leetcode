#!/usr/bin/env python3

from typing import Mapping, List


class Solution:

    cache = {}

    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        elif n == 1:
            return ['()']
        elif n in self.cache:
            return self.cache[n]

        res = []
        for i in range(n):
            sub1 = self.generateParenthesis(i)
            sub2 = self.generateParenthesis(n-i-1)

            if not sub1:
                res1 = ['()']
            else:
                res1 = [f'({s})' for s in sub1]

            if not sub2:
                res += res1
            else:
                for s1 in res1:
                    for s2 in sub2:
                        res.append(f'{s1}{s2}')

        self.cache[n] = res
        return res
