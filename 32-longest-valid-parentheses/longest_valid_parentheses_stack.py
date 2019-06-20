#!/usr/bin/env python3


class Solution:

    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        stack = []
        res = 0

        for i in range(0, n):
            # print(stack)
            if s[i] == '(':
                if not (stack and stack[-1] != '('):
                    stack.append(0)
                stack.append('(')
            else:
                count = 0

                if stack and stack[-1] != '(':
                    count += stack.pop(-1)

                if stack and stack[-1] == '(':
                    stack.pop(-1)
                    count += 2

                    count += stack.pop(-1)
                    res = max(res, count)

                    stack.append(count)
                else:
                    stack = []

        return res
