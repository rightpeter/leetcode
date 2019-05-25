#!/usr/bin/env python3

from typing import List


def twoCommonPrefix(s1, s2: str) -> str:
    prefix = ""
    for i in range(0, min(len(s1), len(s2))):
        if s1[i] == s2[i]:
            prefix += s1[i]
        else:
            break

    return prefix


class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        c = 1
        d = 2 * c
        n = len(strs)

        if n == 0:
            return ""

        while c < n:
            for i in range(0, n, d):
                j = i + c
                if j > n - 1:
                    continue
                if strs[i] == "" or strs[j] == "":
                    return ""

                strs[i] = twoCommonPrefix(strs[i], strs[j])

            c *= 2
            d *= 2

        return strs[0]
