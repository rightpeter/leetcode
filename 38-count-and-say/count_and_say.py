#!/usr/bin/env python3


class Solution:
    def next(self, prev: str) -> str:
        # print(f'prev: {prev}')
        res = ''
        curr = prev[0]
        count = 1

        for c in prev[1:]:
            if c == curr:
                count += 1
            else:
                res += f'{count}{curr}'
                curr = c
                count = 1

        res += f'{count}{curr}'

        return res

    def countAndSay(self, n: int) -> str:
        table = {}
        res = '1'
        table[1] = res
        # print(f'1: 1')

        for i in range(2, n + 1):
            res = self.next(res)
            # print(f'{i}: {res}')
            table[i] = res

        # print(f'tabla: {table}')
        return res
