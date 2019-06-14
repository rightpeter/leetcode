#!/usr/bin/env python3

from typing import List

class Solution:

    def matchWords(self, target, words_dict, n):
        while target:
            if words_dict.get(target[:n], 0) > 0:
                words_dict[target[:n]] = words_dict[target[:n]] - 1
                target = target[n:]
            else:
                return False

        return True


    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        words_dict = {}

        for word in words:
            words_dict[word] = words_dict.get(word, 0) + 1

        n = len(words[0])

        res = []
        for i in range(len(s)-len(words)*n+1):
            if self.matchWords(s[i:i+len(words)*n], words_dict.copy(), n):
                res.append(i)

        return res
