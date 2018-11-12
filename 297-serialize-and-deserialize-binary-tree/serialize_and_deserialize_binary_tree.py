class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import json

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ans = []
        queue = []
        if root is not None:
            queue.append([0, root])
        
        while len(queue) > 0:
            task = queue.pop(0)
            ans.append([task[0], task[1].val])
            if task[1].left is not None:
                queue.append([task[0]*2+1, task[1].left])
            if task[1].right is not None:
                queue.append([task[0]*2+2, task[1].right])
        
        return json.dumps(ans)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        json_tree = json.loads(data)

        hash_table = {}
        root = None

        # print("data: ", data)
        if len(json_tree) > 0:
            node = json_tree.pop(0)
            root = TreeNode(node[1])
            hash_table[0] = root
        
        for node in json_tree:
            parent = (node[0] + 1) / 2 - 1 if node[0] % 2 == 1 else node[0] / 2 - 1
            # print("parent: ", parent)
            tree_node = TreeNode(node[1])
            hash_table[node[0]] = tree_node
            if node[0] % 2 == 1:
                hash_table[parent].left = tree_node
            else:
                hash_table[parent].right = tree_node
        
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))