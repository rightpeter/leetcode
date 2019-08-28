#!/usr/bin/env python3

from typing import List
from tree_helper import TreeNode


class Solution:

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def traversal(root: TreeNode):
            if not root:
                return []

            res = []

            res = traversal(root.left)
            res.append(root.val)
            res += traversal(root.right)

            return res

        return traversal(root)
