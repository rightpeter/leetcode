#!/usr/bin/env python3

from bin_tree_helper import TreeNode


class Solution:

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        count = 0
        res = root.val

        def mid_order(root: TreeNode):
            nonlocal count
            nonlocal res

            if not root:
                return

            if count >= k:
                return

            mid_order(root.left)

            if count >= k:
                return

            count += 1
            if count == k:
                res = root.val
                return

            mid_order(root.right)

        mid_order(root)
        return res
