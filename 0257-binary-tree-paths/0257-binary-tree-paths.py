# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        
        def backtrack(path, root):
            path.append(str(root.val))
            if not (root.left or root.right):
                result.append(path)
                return
            if root.left:
                backtrack(path.copy(), root.left)
            if root.right:
                backtrack(path.copy(), root.right)
        backtrack([], root)
        return ['->'.join(path) for path in result]