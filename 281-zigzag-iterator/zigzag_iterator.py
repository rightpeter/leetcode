#!/usr/bin/env python3


class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        if len(v1) > len(v2):
            self.v1 = v1
            self.v2 = v2
            self.firstv = True
        else:
            self.v1 = v2
            self.v2 = v1
            if len(self.v2) > 0:
                self.firstv = False
            else:
                self.firstv = True

        self.i = 0
        self.j = 0

    def next(self):
        """
        :rtype: int
        """
        if self.firstv:
            res = self.v1[self.i]
            self.i += 1
            if self.j < len(self.v2):
                self.firstv = False
        else:
            res = self.v2[self.j]
            self.j += 1
            self.firstv = True

        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.i < len(self.v1) or self.j < len(self.v2)
