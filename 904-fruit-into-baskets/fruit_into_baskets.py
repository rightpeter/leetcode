#!/usr/bin/env python3

from typing import List


class Solution:

    def totalFruit(self, tree: List[int]) -> int:
        basket = {}
        count = 0
        res = 0

        i = -1
        for j in range(len(tree)):
            # print(f'count: {count}')
            # print(f'basket: {basket}')
            if count < 2:
                if tree[j] in basket:
                    basket[tree[j]] += 1
                else:
                    basket[tree[j]] = 1
                    count += 1
            elif count == 2:
                if tree[j] in basket:
                    basket[tree[j]] += 1
                else:
                    tmp_res = 0
                    for t in basket:
                        tmp_res += basket[t]

                    res = max(res, tmp_res)

                    while count == 2:
                        i += 1
                        basket[tree[i]] -= 1
                        if basket[tree[i]] == 0:
                            del(basket[tree[i]])
                            count -= 1

                    basket[tree[j]] = 1
                    count += 1

        # print(f'count: {count}')
        # print(f'basket: {basket}')

        tmp_res = 0
        for t in basket:
            tmp_res += basket[t]

        res = max(res, tmp_res)

        return res
