#!/usr/bin/env python3

from typing import List, T

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class NodeListHelper:

    @staticmethod
    def list_to_node_list(xs: List[T]) -> ListNode:
        if not len(xs):
            return None

        head = ListNode(xs[0])
        tail = head

        for x in xs[1:]:
            tail.next = ListNode(x)
            tail = tail.next

        return head

    @staticmethod
    def node_list_to_list(head: ListNode) -> List[T]:
        res = []

        while head:
            res.append(head.val)
            head = head.next

        return res

    @staticmethod
    def print_node_list(head: ListNode) -> str:
        if not head:
            return ''

        res = f'{head.val}'

        while head.next:
            head = head.next
            res += f' -> {head.val}'

        return res

    @staticmethod
    def compare_two_node_list(l1, l2: ListNode) -> bool:
        while l1 and l2:
            if l1.val != l2.val:
                return False

            l1 = l1.next
            l2 = l2.next

        if l1 or l2:
            return False

        return True


