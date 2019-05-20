#!/usr/bin/env python3

Digit_Map = {1: ['I', 'X', 'C', 'M'], 5: ['V', 'L', 'D']}


def get_Roma_digit(x, d: int) -> str:
    if x == 0:
        return ''
    elif 1 <= x <= 3:
        return Digit_Map[1][d] * x
    elif x == 4:
        return f'{Digit_Map[1][d]}{Digit_Map[5][d]}'
    elif 5 <= x <= 8:
        return Digit_Map[5][d] + Digit_Map[1][d] * (x - 5)
    elif x == 9:
        return f'{Digit_Map[1][d]}{Digit_Map[1][d+1]}'


class Solution:

    def intToRoman(self, num: int) -> str:
        res = ''
        d = 0

        while num > 0:
            x = num % 10
            R_digit = get_Roma_digit(x, d)
            res = R_digit + res
            num = num // 10
            d += 1

        return res
