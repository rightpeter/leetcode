#!/usr/bin/env python3


class Solution:

    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ans = [-1, len(s)]
        char_set = {}
        char_count = {}
        char_std = {}

        for char in t:
            char_count[char] = 0
            if char not in char_set:
                char_std[char] = 1
                char_set[char] = 1
            else:
                char_std[char] += 1
                char_set[char] += 1

        i = 0
        j = 0

        while i < len(s) and j < len(s):
            while j < len(s) and len(char_set) > 0:
                if s[j] in char_set:
                    char_set[s[j]] -= 1
                    if char_set[s[j]] == 0:
                        del(char_set[s[j]])

                if s[j] in char_count:
                    char_count[s[j]] += 1

                j += 1

            if len(char_set) == 0:
                while s[i] in char_std and char_count[s[i]] > char_std[s[i]] or s[i] not in char_std:
                    if s[i] in char_std:
                        char_count[s[i]] -= 1
                    i += 1

                if j - i < ans[1] - ans[0]:
                    ans = [i, j]

                char_count[s[i]] -= 1
                char_set[s[i]] = 1
                i += 1

        if len(char_set) == 0:
            if j - i < ans[1] - ans[0]:
                ans = [i, j]

        if ans[1] - ans[0] > len(s):
            return ""
        else:
            return s[ans[0]: ans[1]]
