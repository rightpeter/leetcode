#!/usr/bin/env python3

from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = 0

        n = len(words)
        while i < n:
            tmp_len = len(words[i])
            j = i
            while j + 1 < n and tmp_len + len(words[j + 1]) + 1 <= maxWidth:
                j += 1
                tmp_len += len(words[j]) + 1

            if j >= n - 1:
                tmp_res = words[i]
                for x in range(i + 1, j + 1):
                    tmp_res += f' {words[x]}'
                tmp_res += ' ' * (maxWidth - len(tmp_res))
                res.append(tmp_res)
            else:
                if j == i:
                    res.append(words[i] + ' ' * (maxWidth - tmp_len))
                else:
                    tmp_count = j - i
                    count = (maxWidth - tmp_len) // tmp_count
                    residual = (maxWidth - tmp_len) % tmp_count

                    tmp_res = words[i]
                    i += 1
                    for _ in range(residual):
                        tmp_res += ' ' * (count + 2) + words[i]
                        i += 1

                    for _ in range(tmp_count - residual):
                        tmp_res += ' ' * (count + 1) + words[i]
                        i += 1
                    res.append(tmp_res)

            i = j + 1

        # for line in res:
            # print(line + '|')

        return res
