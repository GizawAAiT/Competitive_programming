# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        path = []
        
        def backtrack(root):
            path.append(str(root.val))
            if not (root.left or root.right):
                result.append(path[:])
                path.pop()
                return
            
            if root.left:
                backtrack(root.left)
            if root.right:
                backtrack(root.right)
            path.pop()
        backtrack(root)
        
        return ['->'.join(path) for path in result]