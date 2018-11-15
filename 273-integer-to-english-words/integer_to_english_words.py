#!/usr/bin/env python3

units = [
    'Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
    'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen',
    'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen'
]
tens = [
    '', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy',
    'Eighty', 'Ninety'
]
divider = ['', 'Thousand', 'Million', 'Billion']


class Solution:

    def print_hundreds(self, num):
        if num % 100 == 0:
            return units[num // 100] + " Hundred"

        ans = ""
        if num >= 100:
            ans += "{} Hundred ".format(units[num // 100])

        ans += self.print_tens(num % 100)

        return ans

    def print_tens(sefl, num):
        if num < 20:
            return units[num]
        elif num % 10 == 0:
            return tens[num // 10]
        else:
            return "{} ".format(tens[num // 10]) + units[num % 10]

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return units[0]

        ans = ""
        stack = []
        while num > 0:
            # print("num: ", num)
            stack.append(num % 1000)
            num //= 1000

        # print(stack)
        while len(stack) > 0:
            num = stack.pop()

            if num == 0:
                continue

            ans += self.print_hundreds(num)
            if len(stack) > 0:
                ans += " {} ".format(divider[len(stack)])

        if ans[-1] == ' ':
            ans = ans[:-1]
        return ans
