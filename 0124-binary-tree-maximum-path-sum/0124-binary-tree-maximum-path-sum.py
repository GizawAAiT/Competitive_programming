# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = float('-inf')
        def recursion(node):
            nonlocal result
            if not node: 
                return 0
            left_sum = recursion(node.left) 
            right_sum = recursion(node.right)
            result = max(result, left_sum + node.val, right_sum + node.val, left_sum + node.val + right_sum, node.val)
            return max(0, left_sum + node.val, right_sum + node.val, node.val)
        recursion(root)
        return result