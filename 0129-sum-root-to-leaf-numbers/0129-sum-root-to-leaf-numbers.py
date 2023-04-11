# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = 0
        
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        path = []
        
        def dfs(root):
            
            path.append(str(root.val))
            
            if not (root.left or root.right):
                self.result += int(''.join(path))
                path.pop()
                return
            
            if root.left:
                dfs(root.left)
            
            if root.right:
                dfs(root.right)
                
            path.pop()
        
        dfs(root)
        
        return self.result
                
         
            
            
            
            