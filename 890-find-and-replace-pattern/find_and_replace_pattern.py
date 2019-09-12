#!/usr/bin/env python3

from typing import List


class Solution:

    def findAndReplacePattern(self, words: List[str],
                              pattern: str) -> List[str]:

        def char_to_int(c: str) -> int:
            return ord(c) - ord('a')

        m = len(pattern)

        res = []
        for word in words:
            # print(f'word: {word}, pattern: {pattern}')
            p = [-1] * 26
            available = [True] * 26

            for i in range(m):
                # print(f'p: \t\t{p}')
                # print(f'available: \t{available}')

                c = char_to_int(word[i])
                # print(f'c: {c}')
                pc = char_to_int(pattern[i])
                # print(f'pc: {pc}')
                if p[c] == -1:
                    if available[pc]:
                        p[c] = pc
                        available[pc] = False
                        continue
                    else:
                        break

                if p[c] != pc:
                    break
            else:
                res.append(word)

        return res
