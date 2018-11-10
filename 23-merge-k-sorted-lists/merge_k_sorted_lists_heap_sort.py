#!/usr/bin/env python2
from Queue import PriorityQueue


class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        ret = ListNode(0)
        p = ret
        q = PriorityQueue()
        for i in lists:
            if i:
                print("i.val: {}, i: {}".format(i.val, i))
                q.put((i.val, i))

        while not q.empty():
            min_val, head = q.get()

            p.next = ListNode(min_val)
            p = p.next
            head = head.next
            if head:
                q.put((head.val, head))

        return ret.next
