#!/usr/bin/env python3

from node_list_helper import ListNode

class Solution:

    def swapPairs(self, head: ListNode) -> ListNode:
        first = ListNode(0)
        first.next = head
        second = first.next
        if second and second.next:
            third = second.next.next
        head = first

        while second and second.next:
            first.next = second.next
            first.next.next = second
            second.next = third

            first = second
            second = third
            if second and second.next:
                third = second.next.next

        return head.next
