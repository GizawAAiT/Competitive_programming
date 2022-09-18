# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:return 0 
        d ={root:1}
        Q=[root]
        mindepth = float("inf")
        while Q:
            l = len(Q)
            for _ in range(l):
                node = Q.pop(0)  
                if not(node.left or node.right) and d[node]<mindepth:
                    mindepth = d[node]
                if node.left:
                    Q.append(node.left)
                    d[node.left] = d[node]+1                    
                if node.right:
                    Q.append(node.right)
                    d[node.right] = d[node]+1                    
                    
        return mindepth