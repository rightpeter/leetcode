#!/usr/bin/env python3


class Solution:

    def evaluate(self, expression: str) -> int:

        def parse_one_value(lo: int, end: str, variables: dict) -> (int, int):
            i = lo
            if expression[i] == '(':
                value, i = parse(i, variables.copy())
                return value, i

            j = i
            while expression[j] != end:
                j += 1
            s1 = expression[i:j]
            return int(s1) if s1.replace('-', '').isnumeric() else variables[s1], j

        def parse(lo: int, variables: dict) -> (int, int):
            i = lo + 1

            j = i
            while expression[j] != ' ':
                j += 1

            command = expression[i:j]
            i = j + 1

            if command == 'let':
                while True:
                    if expression[i] == '(':
                        val, i = parse(i, variables.copy())
                        return val, i + 1

                    j = i
                    while expression[j] != ' ' and expression[j] != ')':
                        j += 1
                    s1 = expression[i:j]
                    if expression[j] == ')':
                        return int(s1) if s1.replace('-', '').isnumeric() else variables[s1], j + 1

                    i = j + 1
                    x2, i = parse_one_value(i, ' ', variables.copy())
                    variables[s1] = x2
                    i += 1
            else:
                x1, i = parse_one_value(i, ' ', variables.copy())
                i += 1
                x2, i = parse_one_value(i, ')', variables.copy())

                if command == 'add':
                    return x1 + x2, i + 1
                else:
                    return x1 * x2, i + 1

        return parse(0, {})[0]
