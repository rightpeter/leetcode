#!/usr/bin/env python3


class Solution:
    def __init__(self):
        self.mem = {}

    def insertMem(self, i, j, value):
        # print("insertMem, i: {}, j: {}, value: {}".format(i, j, value))
        if i not in self.mem:
            self.mem[i] = {}

        self.mem[i][j] = value
        # print("self.mem[i][j]: ", self.mem[i][j])

    def isMatch(self, s, p):
        # print("isMatch, s: {}, p: {}".format(s, p))
        ls = len(s)
        lp = len(p)
        if ls in self.mem and lp in self.mem[ls]:
            # print("return self.mem[{}][{}]: {}".format(ls, lp, self.mem[ls][lp]))
            return self.mem[ls][lp]

        if not p:
            # print("insert ls: {}, lp: {}\n self.mem: {}".format(ls, lp, self.mem))
            self.insertMem(ls, lp, not s)
            # print("return self.mem[{}][{}]: {}".format(ls, lp, self.mem[ls][lp]))
            return self.mem[ls][lp]

        first_match = bool(s) and p[0] in [s[0], '.']
        if len(p) > 1 and p[1] == '*':
            # print("insert ls: {}, lp: {}\n self.mem: {}".format(ls, lp, self.mem))
            self.insertMem(
                ls, lp,
                self.isMatch(s, p[2:]) or
                first_match and self.isMatch(s[1:], p))
            # print("return self.mem[{}][{}]: {}".format(ls, lp, self.mem[ls][lp]))
            return self.mem[ls][lp]
        else:
            # print("insert ls: {}, lp: {}\n self.mem: {}".format(ls, lp, self.mem))
            self.insertMem(ls, lp, first_match and self.isMatch(s[1:], p[1:]))
            # print("return self.mem[{}][{}]: {}".format(ls, lp, self.mem[ls][lp]))
            return self.mem[ls][lp]
