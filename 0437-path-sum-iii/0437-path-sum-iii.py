# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], target: int) -> int:
        path = []
        
        answer = 0
        
        def backtrack(node):
            if not node:
                return
            
            nonlocal answer
            path.append(node.val)
                 
            total = 0
            for val in path[::-1]: 
                total += val 
                if total == target: 
                    answer += 1 
                    
            backtrack(node.left)
            backtrack(node.right)
            path.pop()
            
        backtrack(root) 
        return answer
            
