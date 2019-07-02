#!/usr/bin/env python3


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        if len(num2) > len(num1):
            num1, num2 = num2, num1

        sum_list = [0 for _ in range(len(num2) + len(num1) + 1)]

        res = ''

        for i in range(1, len(num2) + 1):
            for j in range(1, len(num1) + 1):
                sum_list[-i - j + 1] += int(num1[-j]) * int(num2[-i])

        # print(f'sum_list: {sum_list}')

        for i in range(1, len(num2) + len(num1) + 1):
            res = str(sum_list[-i] % 10) + res
            sum_list[-i - 1] += sum_list[-i] // 10
            # print(f'i: {i}, res: {res}, sum_list: {sum_list}')

        if res[0] != '0':
            return res

        i = 0
        while i < len(res) and res[i] == '0':
            i += 1

        if i >= len(res):
            return '0'
        else:
            res = res[1:]

        return res
