#!/usr/bin/env python3

from node_list_helper import ListNode
from node_list_helper import NodeListHelper


class Solution:

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        left = ListNode(0)
        left.next = head
        head = left

        while True:
            if not left:
                return head.next

            tail = left
            for _ in range(k):
                tail = tail.next
                if not tail:
                    return head.next

            first = left

            second = first.next
            if not second:
                return head.next

            third = second.next

            for i in range(k-1):
                first = second

                second = third
                if not second:
                    left.next.next = None
                    left.next = first
                    return head.next

                third = second.next

                second.next = first

            left.next.next = third
            first = left.next
            left.next = second

            left = first

        return head.next
