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
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        ans = []

        def process(root: TreeNode, parent: bool):
            if root is None:
                return

            if not parent and root.val not in to_delete:
                ans.append(root)

            if root.val in to_delete:
                parent = False
            else:
                parent = True

            left = root.left
            right = root.right

            if left:
                if left.val in to_delete:
                    root.left = None
                process(left, parent)

            if right:
                if right.val in to_delete:
                    root.right = None
                process(right, parent)

        process(root, False)
        return ans
