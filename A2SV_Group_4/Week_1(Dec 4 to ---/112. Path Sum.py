# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], target: int) -> bool:
        if not root:
            return False
        d = {root:root.val}
        Q = [root]
        while Q:
            node = Q.pop(0)
            if not node.left and not node.right and d[node]==target:
                return True
            if node.left:
                d[node.left]=d[node]+node.left.val
                Q.append(node.left)
            if node.right:
                d[node.right]=d[node]+node.right.val
                Q.append(node.right)
        return False