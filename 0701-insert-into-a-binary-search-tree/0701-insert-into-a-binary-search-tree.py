# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: return TreeNode(val)
        t = root
        while t.left or t.right:
            if val < t.val and not t.left:
                t.left = TreeNode(val)
                return root
            
            if val > t.val and not t.right:
                t.right = TreeNode(val)
                return root
            if val < t.val:
                
                t = t.left
            else:
                t = t.right
        if val < t.val:
            t.left = TreeNode(val)  
        else:
            t.right = TreeNode(val)
        return root