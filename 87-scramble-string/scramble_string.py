#!/usr/bin/env python3

from collections import Counter


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        def is_scramble(s1, s2: str) -> bool:
            # print(f's1: {s1}, s2: {s2}')
            if len(s1) != len(s2):
                return False

            n = len(s1)

            if n == 0:
                return True

            if n == 1:
                return s1[0] == s2[0]

            cs1 = Counter()
            cs2a = Counter()
            cs2b = Counter()

            for i in range(n - 1):
                cs1[s1[i]] += 1
                cs2a[s2[i]] += 1
                cs2b[s2[n - 1 - i]] += 1

                if cs1 == cs2a:
                    if is_scramble(s1[:i + 1], s2[:i + 1]) and is_scramble(s1[i + 1:], s2[i + 1:]):
                        return True
                if cs1 == cs2b:
                    if is_scramble(s1[:i + 1], s2[n - 1 - i:]) and is_scramble(s1[i + 1:], s2[:n - 1 - i]):
                        return True

            return False

        return is_scramble(s1, s2)
