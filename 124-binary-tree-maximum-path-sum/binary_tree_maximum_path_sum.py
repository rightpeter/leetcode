#!/usr/bin/env python3

from bin_tree_helper import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def maxPathSum(self, root: TreeNode) -> int:
        res = root.val

        def findMax(root: TreeNode) -> int:
            nonlocal res
            if root.left:
                max_left = findMax(root.left)
            else:
                max_left = 0
            max_left = max(max_left, 0)

            if root.right:
                max_right = findMax(root.right)
            else:
                max_right = 0
            max_right = max(max_right, 0)

            root_max = max_left + max_right + root.val
            if root_max > res:
                res = root_max

            return max(max_left, max_right) + root.val

        findMax(root)

        return res
