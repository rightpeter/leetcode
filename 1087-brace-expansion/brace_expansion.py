#!/usr/bin/env python3

from typing import List


class Solution:

    def expand(self, S: str) -> List[str]:
        if not S:
            return []

        res = []

        i = 0
        while i < len(S):
            if S[i] == '{':
                i += 1
                char_list = []
                while S[i] != '}':
                    if S[i] != ',':
                        char_list.append(S[i])
                    i += 1
                i += 1

                if not res:
                    res = char_list
                else:
                    new_res = []
                    for c in char_list:
                        new_res += [s + c for s in res]

                    res = new_res
            else:
                if not res:
                    res = [S[i]]
                else:
                    res = [s + S[i] for s in res]
                i += 1

        res.sort()
        return res
