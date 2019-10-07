#!/usr/bin/env python3

from typing import List


class Solution:

    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        res = 0
        i = 0
        j = 0
        k = 0

        mem = {}
        sentence = [len(w) for w in sentence]
        n = len(sentence)

        while i < rows:
            if k in mem:
                res += mem[k][0]
                k = mem[k][1]
                i += 1
                continue

            start_k = k
            start_res = res

            # print(f'i: {i}')
            if sentence[k] > cols:
                return 0

            j = sentence[k]
            # print(sentence[k], end='')
            k += 1
            if k == n:
                res += 1
                k = 0

            while j + sentence[k] + 1 <= cols:
                j += sentence[k] + 1

                # print('-' + sentence[k], end='')

                k += 1
                if k == n:
                    res += 1
                    k = 0

            mem[start_k] = [res - start_res, k]
            i += 1
            # print('-' * (cols - j))
            j = 0

        return res
