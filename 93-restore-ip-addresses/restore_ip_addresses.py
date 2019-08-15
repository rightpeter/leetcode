#!/usr/bin/env python3

from typing import List


class Solution:

    def restoreIpAddresses(self, s: str) -> List[str]:

        def valid_number(num: str):
            if not num:
                return False

            if num == '0':
                return True

            i = 0
            while i < len(num) and num[i] == '0':
                i += 1
            if i:
                return False

            return 0 <= int(num) <= 255

        def dfs(lo, m: int):
            if m == 1:
                if valid_number(s[lo:]):
                    return [s[lo:]]
                else:
                    return []

            res = []

            for i in range(lo + 1, min(len(s), lo + 4)):
                if valid_number(s[lo:i]):
                    res += [s[lo:i] + '.' + x for x in dfs(i, m - 1)]

            return res

        return dfs(0, 4)
