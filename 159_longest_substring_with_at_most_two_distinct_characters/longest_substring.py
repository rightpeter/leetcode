#!/usr/bin/env python3


class Solution:

    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        window = []
        i = 0
        j = 0
        t_len = 0
        max_sum = 0

        while i < len(s) and j < len(s):
            if s[j] in window:
                t_len += 1
            elif s[j] not in window:
                if len(window) < 2:
                    window.append(s[j])
                    t_len += 1
                else:
                    if t_len > max_sum:
                        max_sum = t_len
                    t_len = 2
                    i = j - 1
                    window = [s[i], s[j]]
                    while i > 0 and s[i - 1] == s[i]:
                        i -= 1
                        t_len += 1

            j += 1

        if t_len > max_sum:
            max_sum = t_len

        return max_sum
