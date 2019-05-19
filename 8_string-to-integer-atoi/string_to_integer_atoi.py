#!/usr/bin/env python3

MAX_INT = 2**31 - 1
MIN_INT = -2**31


def is_number(c: str) -> bool:
    return ord(c) >= ord('0') and ord(c) <= ord('9')


class Solution:

    def myAtoi(self, input_str: str) -> int:
        if len(input_str) == 0:
            return 0

        i = 0
        while i < len(input_str) and input_str[i] == ' ':
            i += 1

        if i == len(input_str):
            return 0

        sign = 1
        if input_str[i] == '-':
            sign = -1
            i += 1
        elif input_str[i] == '+':
            i += 1
        elif ord(input_str[i]) < ord('0') and ord(input_str[i]) > ord('9'):
            return 0

        res = 0
        while i < len(input_str) and is_number(input_str[i]):
            res = 10 * res + sign * int(input_str[i])
            # print(f"i: {i}, res: {res}")
            if res < MIN_INT:
                res = MIN_INT
                break
            if res > MAX_INT:
                res = MAX_INT
                break
            i += 1
        return res
