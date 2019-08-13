#!/usr/bin/env python3

from node_list_helper import ListNode


class Solution:

    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head

        h = ListNode(0)
        h.next = head

        lo = h
        for _ in range(m - 1):
            lo = lo.next

        p1 = lo.next
        p2 = p1.next
        for _ in range(n - m - 1):
            tmp = p2.next
            p2.next = p1
            p1 = p2
            p2 = tmp

        lo.next.next = p2.next
        lo.next = p2
        p2.next = p1

        return h.next
