#!/usr/bin/env python3


class Solution:

    def reverseOnlyLetters(self, S: str) -> str:
        if not S:
            return S

        i = 0
        j = len(S) - 1
        res = list(S)

        while i < j:
            while i < j and not res[i].isalpha():
                i += 1
            while i < j and not res[j].isalpha():
                j -= 1

            if i < j:
                res[i], res[j] = res[j], res[i]
                i += 1
                j -= 1

        return ''.join(res)
