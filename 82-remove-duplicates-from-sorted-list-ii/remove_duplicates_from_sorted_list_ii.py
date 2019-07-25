#!/usr/bin/env python3

from node_list_helper import ListNode


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        p = ListNode(0)
        p.next = head

        curr = p
        while curr.next:
            tail = curr.next
            while tail.next and tail.next.val == tail.val:
                tail = tail.next
            if curr.next != tail:
                curr.next = tail.next
            else:
                curr = curr.next
        return p.next
