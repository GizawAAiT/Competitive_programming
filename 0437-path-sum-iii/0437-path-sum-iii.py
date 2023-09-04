# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], target: int) -> int:
        cum = 0

        answer = 0
        dic = defaultdict(int)
        dic[0] = 1
        def backtrack(node):
            
            if not node:
                return
            
            nonlocal answer
            nonlocal cum
            
            cum += node.val
            left = cum - target 
            answer += dic[left] 
            dic[cum] += 1
            
            backtrack(node.left)
            backtrack(node.right)
            dic[cum] -= 1 
            cum -= node.val
            
        backtrack(root) 
        return answer
            
