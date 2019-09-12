#!/usr/bin/env python3

from bin_tree_helper import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def isValidBST(self, root: TreeNode) -> bool:

        def validate(root: TreeNode) -> (bool, int, int):
            left_lo = root.val
            left_hi = root.val - 1
            right_lo = root.val + 1
            right_hi = root.val

            if root.left:
                res, lo, hi = validate(root.left)
                if not res:
                    return (False, left_lo, right_hi)

                left_lo = lo
                left_hi = hi

            if root.right:
                res, lo, hi = validate(root.right)
                if not res:
                    return (False, left_lo, right_hi)

                right_lo = lo
                right_hi = hi

            if root.val > left_hi and root.val < right_lo:
                return (True, left_lo, right_hi)

            return (False, left_lo, right_hi)

        if not root:
            return True

        return validate(root)[0]
