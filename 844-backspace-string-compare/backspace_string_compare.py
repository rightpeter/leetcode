#!/usr/bin/env python3


class Solution:

    def backspaceCompare(self, S: str, T: str) -> bool:

        def process(S: str) -> str:
            stack = [0] * len(S)
            i = 0
            for c in S:
                if c == '#':
                    i = max(i - 1, 0)
                else:
                    stack[i] = c
                    i += 1

            return stack[:i]

        s = process(S)
        t = process(T)

        return s == t
