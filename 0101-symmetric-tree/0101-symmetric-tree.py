# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def bulshit(r1, r2):
            if not(r1 or r2)  : # 
                return True
            if not (r1 and r2):  #
                return False
            if r1.val != r2.val:
                return False
            return bulshit(r1.left, r2.right) and bulshit(r1.right, r2.left) 
        
        if not root :
            return True 
        return bulshit(root.left, root.right)

