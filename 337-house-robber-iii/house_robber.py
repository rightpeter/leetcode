#!/usr/bin/env python3

from bin_tree_helper import TreeNode
from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def rob(self, root: TreeNode) -> int:

        def max_value(root: TreeNode) -> List[int]:
            if not root:
                return [0, 0]

            left = max_value(root.left)
            right = max_value(root.right)

            return [
                max([
                    left[0] + right[0], left[0] + right[1], left[1] + right[0],
                    left[1] + right[1]
                ]), root.val + left[0] + right[0]
            ]

        return max(max_value(root))
