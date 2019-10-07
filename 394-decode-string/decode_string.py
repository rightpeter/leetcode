#!/usr/bin/env python3


def is_number(c: str) -> bool:
    return c in {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}


class Solution:

    def decodeString(self, s: str) -> str:
        res = ''
        i = 0
        while i < len(s):
            if is_number(s[i]):
                num = int(s[i])
                i = i + 1
                while is_number(s[i]):
                    num = 10 * num + int(s[i])
                    i += 1

                i += 1
                j = i
                count = 0
                while count != 0 or s[j] != ']':
                    if s[j] == '[':
                        count += 1
                    if s[j] == ']':
                        count -= 1
                    j += 1
                ts = self.decodeString(s[i:j])
                res += ts * num
                i = j + 1
            else:
                j = i
                while j < len(s) and not is_number(s[j]):
                    j += 1
                res += s[i:j]
                i = j

        return res
