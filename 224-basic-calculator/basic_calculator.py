#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:

    def readNumber(self, s, i):
        ans = int(s[i])
        i += 1
        while i < len(s) and s[i] >= '0' and s[i] <= '9':
            ans *= 10
            ans += int(s[i])
            i += 1
        return ans, i

    def combine(self, a, sign, b):
        if sign == '+':
            return a + b
        elif sign == '-':
            return a - b

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        s = s.replace(' ', '')
        s = '(' + s + ')'
        num_stack = []
        sign_stack = []

        i = 0
        tmp_sum = None
        sign = None
        while i < len(s):
            # print("i: {}, num_stack: {}, sign_stack: {}".format(i, num_stack, sign_stack))
            if s[i] >= '0' and s[i] <= '9':
                num, i = self.readNumber(s, i)
                if tmp_sum is None:
                    tmp_sum = num
                else:
                    tmp_sum = self.combine(tmp_sum, sign, num)
                    # sign = None
                continue
            elif s[i] == '+' or s[i] == '-':
                sign = s[i]
                i += 1
                continue
            elif s[i] == '(':
                if tmp_sum is not None:
                    num_stack.append(tmp_sum)
                    sign_stack.append(sign)
                    tmp_sum = None
                    # sign = None
                num_stack.append('(')
                i += 1
                continue
            elif s[i] == ')':
                num = num_stack.pop()
                if num != '(':
                    sign = sign_stack.pop()
                    tmp_sum = self.combine(num, sign, tmp_sum)
                    num = num_stack.pop()
                if len(num_stack) > 0:
                    num = num_stack.pop()
                    if num != '(':
                        sign = sign_stack.pop()
                        tmp_sum = self.combine(num, sign, tmp_sum)
                    else:
                        num_stack.append('(')
                i += 1
                continue

        return tmp_sum if tmp_sum is not None else 0
