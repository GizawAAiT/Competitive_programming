# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: 
            return root
        
        if root.val == key:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            t = root.right
            while t.left:
                t = t.left
            root.val = t.val
            root.right = self.deleteNode(root.right, t.val)
        
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        
        return root
