#!/usr/bin/env python3


class Solution:

    def elementMatch(self, e1, e2):
        if e1 == e2 or e2 == '.':
            return True
        else:
            return False

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        patterns = []
        for e in p:
            if e == '*':
                patterns[-1][1] = True
            else:
                patterns.append([e, False])
        # print("patterns: {}".format(patterns))

        match = True
        i = 0
        j = 0
        pre_star = [None, 0]
        while i < len(s) and j < len(patterns):
            if patterns[j][1]:
                while i < len(s) and self.elementMatch(s[i], patterns[j][0]):
                    if s[i] == pre_star[0]:
                        pre_star[1] += 1
                    else:
                        pre_star[0] = s[i]
                        pre_star[1] = 1
                    i += 1
                j += 1
            else:
                # print("i: {}, j: {}, patterns: {}, pre_star: {}".format(i, j, patterns, pre_star))
                if patterns[j][0] == pre_star[0]:
                    if pre_star[1] > 0:
                        pre_star[1] -= 1
                        j += 1
                        continue
                    else:
                        match = False
                        break

                pre_star = [None, 0]
                if self.elementMatch(s[i], patterns[j][0]):
                    i += 1
                    j += 1
                else:
                    match = False
                    break

        # print("i: {}, j: {}, match: {}, pre_star: {}".format(i, j, match, pre_star))
        if i == len(s):
            while match and j < len(patterns):
                if patterns[j][1]:
                    j += 1
                else:
                    if patterns[j][0] == pre_star[0]:
                        if pre_star[1] > 0:
                            pre_star[1] -= 1
                            j += 1
                            continue
                        else:
                            match = False
                            break
                    else:
                        match = False
                        break

        if not (i == len(s) and j == len(patterns)):
            match = False
        if match:
            return True
        else:
            return False
