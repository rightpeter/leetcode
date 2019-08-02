#!/usr/bin/env python3

from node_list_helper import ListNode


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return head

        p = ListNode(0)
        p.next = head

        lo = p
        hi = p

        while hi and hi.next:
            # print(f'lo.val: {lo.val}, hi.val: {hi.val}')
            if hi.next.val < x:
                if hi.next != lo.next:
                    lo.next, hi.next.next, hi.next = hi.next, lo.next, hi.next.next
                else:
                    hi = hi.next
                lo = lo.next
            else:
                hi = hi.next
            # print(NodeListHelper.node_list_to_list(p))
        return p.next
