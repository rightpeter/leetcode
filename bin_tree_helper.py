#!/usr/bin/env python3

from typing import List, T


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class TreeHelper:

    @staticmethod
    def list_to_tree(xs: List[T]) -> TreeNode:
        if not len(xs):
            return None

        root = TreeNode(xs[0]) if xs[0] else None

        queue = [root]

        i = 1
        while i < len(xs):
            queue[0].left = TreeNode(xs[i]) if xs[i] else None
            if xs[i]:
                queue = queue + [queue[0].left]
            i += 1

            if i < len(xs):
                queue[0].right = TreeNode(xs[i]) if xs[i] else None
                if xs[i]:
                    queue = queue + [queue[0].right]
            i += 1

            queue = queue[1:]

        return root

    @staticmethod
    def tree_to_list(root: TreeNode) -> List[T]:
        if not root:
            return []

        res = [root.val]

        queue = [root]
        empty = True

        while queue:
            next_res = []
            next_queue = []
            for node in queue:
                if node.left:
                    next_res.append(node.left.val)
                    next_queue.append(node.left)
                    empty = False
                else:
                    next_res.append(None)

                if node.right:
                    next_res.append(node.right.val)
                    next_queue.append(node.right)
                    empty = False
                else:
                    next_res.append(None)

            # print(f'next_res: {next_res}')

            if empty:
                break

            res += next_res

            queue = next_queue
            empty = True

        i = len(res) - 1
        while not res[i]:
            i -= 1

        return res[:i + 1]

    @staticmethod
    def print_tree(root: TreeNode) -> str:
        if not root:
            return 'None\n'

        res = f'{root.val}\n'
        queue = [root.left, root.right]

        while queue:
            empty = True
            new_res = ''
            new_queue = []
            for node in queue:
                if node:
                    new_res += f'{node.val}\t'
                    new_queue.append(node.left)
                    new_queue.append(node.right)
                    empty = False
                else:
                    new_res += 'None\t'
                    new_queue.append(None)
                    new_queue.append(None)

            if empty:
                break

            res += new_res + '\n'
            queue = new_queue

        return res

    @staticmethod
    def inorder_traversal(root: TreeNode) -> str:
        if not root:
            return []

        res = TreeHelper.inorder_traversal(root.left)
        res.append(root.val)
        res += TreeHelper.inorder_traversal(root.right)

        return res
