#!/usr/bin/env python3


class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        ans = []
        queue = []
        if root is not None:
            queue.append(root)

        while len(queue) > 0:
            task = queue.pop(0)
            if task is not None:
                ans.append(str(task.val))
                queue.append(task.left)
                queue.append(task.right)
            else:
                ans.append("null")

        if len(ans) > 0:
            i = len(ans) - 1
            while i >= 0 and ans[i] == 'null':
                i -= 1
            ans = ans[:i + 1]
        return '[' + ','.join(ans) + ']'

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        data = data[1:-1].split(',')
        root = None
        queue = []

        # print("data: ", data)
        num = data.pop(0)
        if num != '':
            root = TreeNode(int(num))
            queue.append(root)

        while len(data) > 0 and len(queue) > 0:
            node = queue.pop(0)
            if len(data) > 0:
                num = data.pop(0)
                if num != 'null':
                    left = TreeNode(int(num))
                    # print("add {} to left of {}".format(num, node.val))
                    node.left = left
                    queue.append(left)
            if len(data) > 0:
                num = data.pop(0)
                if num != 'null':
                    right = TreeNode(int(num))
                    # print("add {} to left of {}".format(num, node.val))
                    node.right = right
                    queue.append(right)

        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
