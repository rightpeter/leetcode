#!/usr/bin/env python3


class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def merge(self, lists1, lists2):
        ret = p = ListNode(0)

        while lists1 and lists2:
            if lists1.val < lists2.val:
                p.next = ListNode(lists1.val)
                p = p.next
                lists1 = lists1.next
            else:
                p.next = ListNode(lists2.val)
                p = p.next
                lists2 = lists2.next

        while lists1:
            p.next = ListNode(lists1.val)
            p = p.next
            lists1 = lists1.next

        while lists2:
            p.next = ListNode(lists2.val)
            p = p.next
            lists2 = lists2.next

        return ret.next

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]
        else:
            mid = int(len(lists) / 2)
            return self.merge(self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:]))
