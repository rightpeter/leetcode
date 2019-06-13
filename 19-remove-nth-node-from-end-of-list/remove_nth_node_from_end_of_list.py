#!/usr/bin/env python3

from node_list_helper import ListNode

class Solution:

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        left = head
        tail = head
        for _ in range(n):
            tail = tail.next
            if not tail:
                return head.next

        while tail.next:
            left = left.next
            tail = tail.next

        left.next = left.next.next

        return head
