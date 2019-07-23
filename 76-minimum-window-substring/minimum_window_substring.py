#!/usr/bin/env python3

from collections import Counter


class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        res = ''

        dict_t = dict(Counter(t))
        window = {}

        l = 0
        r = 0
        tmp_dict_t = dict_t.copy()
        while tmp_dict_t and r < len(s):
            # print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            # print(f'tmp_dict_t: {tmp_dict_t}\nl: {l}, r: {r}, res: {s[l: r]}\nwindow: {window}')
            c = s[r]
            if c in dict_t:
                window[c] = window.get(c, 0) + 1

            if c in tmp_dict_t:
                tmp_dict_t[c] -= 1
                if not tmp_dict_t[c]:
                    del(tmp_dict_t[c])

            r += 1

        # print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        # print(f'tmp_dict_t: {tmp_dict_t}\nl: {l}, r: {r}, res: {s[l: r]}\nwindow: {window}')
        if tmp_dict_t:
            return ''

        while s[l] not in dict_t or window.get(s[l], 0) > dict_t[s[l]]:
            if s[l] in dict_t:
                window[s[l]] -= 1
            l += 1

        res = s[l:r]
        # print(f'init res: {res}')

        while r < len(s):
            # print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            # print(f'l: {l}, r: {r}, res: {s[l: r]}\nwindow: {window}')
            c = s[r]
            if c in dict_t:
                window[c] += 1

                r += 1

                while s[l] not in dict_t or window.get(s[l], 0) > dict_t[s[l]]:
                    if s[l] in dict_t:
                        window[s[l]] -= 1
                    l += 1

                if r - l < len(res):
                    res = s[l:r]
            else:
                r += 1

        return res
