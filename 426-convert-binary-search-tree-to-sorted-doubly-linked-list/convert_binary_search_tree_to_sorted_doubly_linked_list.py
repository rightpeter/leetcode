#!/usr/bin/env python3


# Definition for a Node.
class Node:

    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def treeToDoublyList(self, root: 'Node') -> 'Node':
        head = None
        tail = None

        def helper(root: 'Node'):
            nonlocal head
            nonlocal tail

            if not root:
                return

            helper(root.left)
            if not head:
                head = root
                tail = root
            else:
                tail.right = root
                root.left = tail
                tail = root
            # self
            helper(root.right)

        helper(root)
        if head:
            head.left = tail

        if tail:
            tail.right = head

        return head
