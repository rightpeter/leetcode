#!/usr/bin/env python3

from tree_helper import TreeNode


class Solution:

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        def isSameNode(n1, n2: TreeNode):
            if not n1 and not n2:
                return True

            if not n1 or not n2:
                return False

            return n1.val == n2.val

        if not isSameNode(p, q):
            return False

        if not p:
            return True

        queue_p = [p]
        queue_q = [q]

        while queue_p and queue_q:
            if not isSameNode(queue_p[0], queue_q[0]):
                return False

            if queue_p[0]:
                queue_p.append(queue_p[0].left)
                queue_q.append(queue_q[0].left)
                queue_p.append(queue_p[0].right)
                queue_q.append(queue_q[0].right)

            queue_p = queue_p[1:]
            queue_q = queue_q[1:]

        return True
