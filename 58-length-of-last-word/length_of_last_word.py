#!/usr/bin/env python3


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] != ' ':
                res += 1
            else:
                if res > 0:
                    break

        return res
