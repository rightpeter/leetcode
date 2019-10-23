#!/usr/bin/env python3

from typing import List
from collections import Counter


class Solution:

    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        p_counter = Counter(p)
        s_counter = Counter(s[:len(p)])

        res = []
        if p_counter == s_counter:
            res = [0]

        for i in range(len(s) - len(p)):
            j = i + len(p)

            if s[i] != s[j]:
                s_counter.update({s[i]: -1, s[j]: 1})

            if s_counter[s[i]] == 0:
                del (s_counter[s[i]])

            if s_counter == p_counter:
                res.append(i + 1)

        return res
