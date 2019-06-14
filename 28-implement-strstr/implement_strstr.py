#!/usr/bin/env python3


class Solution:

    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        for i in range(len(haystack)-len(needle)+1):
            equal = True
            if haystack[i] == needle[0]:
                for j in range(1, len(needle)):
                    if haystack[i+j] != needle[j]:
                        equal = False
                        break

                if equal:
                    return i

        return -1
