# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        left = -1
        Q = [root]
        res = []
        while len(Q) > left+1:
            n = len(Q) - left-1
            level = []
            for i in range(n):
                left += 1
                node = Q[left]
                
                level.append(node.val) 
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
            res.append(level)
        return res