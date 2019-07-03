#!/usr/bin/env python3

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def sort_string(s: str):
            return ''.join(sorted(s))

        str_hash = {}

        for s in strs:
            ss = sort_string(s)

            if ss not in str_hash:
                str_hash[ss] = []

            str_hash[ss].append(s)

        # print(f'str_hash: {str_hash}')
        res = []
        for v in str_hash:
            res.append(str_hash[v])
        return res
