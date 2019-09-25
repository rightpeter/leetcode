#!/usr/bin/env python3

from bin_tree_helper import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:

        def isEquiv(root1: TreeNode, root2: TreeNode) -> bool:
            if root1 == root2 is None:
                return True

            if root1 is None or root2 is None:
                return False

            if root1.val != root2.val:
                return False

            child1 = []
            child2 = []

            if root1.left:
                child1.append(-root1.left.val)
            if root1.right:
                child1.append(root1.right.val)
            if root2.left:
                child2.append(-root2.left.val)
            if root2.right:
                child2.append(root2.right.val)

            if len(child1) != len(child2):
                return False

            if sorted([abs(x) for x in child1]) != sorted([abs(x) for x in child2]):
                return False

            if child1 != child2:
                root2.left, root2.right = root2.right, root2.left

            if isEquiv(root1.left, root2.left) and isEquiv(root1.right, root2.right):
                return True
            return False

        return isEquiv(root1, root2)
