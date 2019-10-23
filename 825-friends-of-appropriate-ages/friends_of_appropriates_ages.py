#!/usr/bin/env python3

from typing import List
from collections import Counter
from itertools import permutations


class Solution:

    def numFriendRequests(self, ages: List[int]) -> int:
        if not ages:
            return 0

        counts = Counter(ages)

        res = 0

        for age, count in counts.items():
            if age > 14:
                res += count * (count - 1)

        for a, b in permutations(counts, 2):
            if b > 0.5 * a + 7 and b <= a:
                res += counts[a] * counts[b]

        return res
