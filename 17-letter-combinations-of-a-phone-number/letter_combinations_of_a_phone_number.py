#!/usr/bin/env python3

from typing import List


class Solution:

    digit_to_letter = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        if len(digits) == 1:
            return self.digit_to_letter[digits[0]]

        tmp_combinations = self.letterCombinations(digits[1:])

        res = []
        for c in self.digit_to_letter[digits[0]]:
            res += [c + s for s in tmp_combinations]

        return res
