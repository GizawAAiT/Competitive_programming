# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return
        
        Q = [root]
        result = []
        while Q:
            
            row = len(Q)
            lev = []
            for i in range(row):
                node = Q.pop(0)
                if node:
                    lev.append(node.val)  
                    Q.append(node.left)
                    Q.append(node.right)
            if lev:
                result.append(lev)
        
        return result
