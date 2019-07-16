#!/usr/bin/env python3


class Solution:
    def isNumber(self, s: str) -> bool:
        l = 0
        while l < len(s) and s[l] == ' ':
            l += 1

        if l == len(s):
            return False

        r = len(s) - 1
        while r >= 0 and s[r] == ' ':
            r -= 1

        valid_char_set = set({'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'e', '.', '+', '-'})

        exponent = False
        exponent_finished = True
        zero = False
        decimal = False
        sign = False
        sign_finished = True
        start = False
        non_zero = False

        for c in s[l:r + 1]:
            if c not in valid_char_set:
                return False
            elif c == '+' or c == '-':
                if sign or start:
                    return False
                else:
                    sign = True
                    sign_finished = False

                if not exponent_finished:
                    exponent_finished = True
            elif c == '0':
                start = True
                zero = True

                if not exponent_finished:
                    exponent_finished = True

                if not sign_finished:
                    sign_finished = True
            elif c == '.':
                if exponent or decimal:
                    return False
                else:
                    decimal = True
                    start = True

                if not exponent_finished:
                    exponent_finished = True

                if not sign_finished:
                    sign_finished = True

            elif c == 'e':
                if decimal and not zero and not non_zero:
                    return False

                if not sign_finished:
                    return False

                if exponent or not start:
                    return False
                else:
                    exponent = True
                    exponent_finished = False
                    start = False
                    sign = False
            else:
                start = True
                non_zero = True

                if not exponent_finished:
                    exponent_finished = True

                if not sign_finished:
                    sign_finished = True

        if decimal and not zero and not non_zero:
            return False

        if not sign_finished:
            return False

        if not exponent_finished:
            return False

        return True
