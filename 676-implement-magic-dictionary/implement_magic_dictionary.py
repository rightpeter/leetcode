#!/usr/bin/env python3

from typing import List


class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}

    def buildDict(self, dic: List[str]) -> None:
        """
        Build a dictionary through a list of words
        """
        for s in dic:
            for i in range(len(s)):
                ns = s[:i] + '*' + s[i + 1:]
                if ns not in self.dic:
                    self.dic[ns] = [s]
                else:
                    self.dic[ns].append(s)

    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """

        # Your MagicDictionary object will be instantiated and called as such:
        # obj = MagicDictionary()
        # obj.buildDict(dict)
        # param_2 = obj.search(word)
        for i in range(len(word)):
            ns = word[:i] + '*' + word[i + 1:]
            if ns in self.dic:
                if len(self.dic[ns]) > 1 or self.dic[ns][0] != word:
                    return True

        return False
