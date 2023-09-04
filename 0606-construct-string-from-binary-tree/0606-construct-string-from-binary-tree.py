# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = ''
        
    def tree2str(self, root: Optional[TreeNode]) -> str:
        self.result = str(root.val)
        
        def dfs(root):
            
            if root.left:
                self.result += f'({root.left.val}'
                dfs(root.left)
                self.result += ')'
            elif root.right:
                self.result += '()'
                
            if root.right:
                self.result += f'({root.right.val}'
                dfs(root.right)
                self.result += ')'
            
        
        dfs(root)
        
        return self.result