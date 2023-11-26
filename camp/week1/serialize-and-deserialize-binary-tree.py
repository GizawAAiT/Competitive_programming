# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return ''

        serialized_data = [str(root.val)]
        leafs = deque([root])
        while leafs:
            node = leafs.popleft()
            left, right = node.left, node.right
            serialized_data.append(str(left.val) if left else 'NULL')
            serialized_data.append(str(right.val) if right else "NULL")
            if left:
                leafs.append(left)
            if right:
                leafs.append(right)
        
        while serialized_data and serialized_data[-1]=='NULL':
            serialized_data.pop()
        
        # print(' '.join(serialized_data))
        return ' '.join(serialized_data)
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split()
        if not data: return None

        root = TreeNode(int(data[0]))
        leafs = deque([root])
        idx = 1
        while idx < len(data) and leafs:
            node = leafs.popleft()
            if data[idx] != 'NULL':
                node.left = TreeNode(int(data[idx]))
                leafs.append(node.left)
            if idx+1 < len(data) and data[idx+1] != 'NULL':
                node.right = TreeNode(int(data[idx+1]))
                leafs.append(node.right)
            idx += 2
        
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))