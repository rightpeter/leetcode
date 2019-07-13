#!/usr/bin/env python3

from node_list_helper import ListNode


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None

        length = 1
        tail = head
        while tail.next:
            length += 1
            tail = tail.next

        # print(f'length: {length}')
        k = k % length

        if k == 0:
            return head

        tail.next = head

        for _ in range(length - k - 1):
            head = head.next

        res, head.next = head.next, None

        return res
