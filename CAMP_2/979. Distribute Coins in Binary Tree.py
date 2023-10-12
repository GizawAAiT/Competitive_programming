# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right 
class Solution:
    def __init__(self):
        self.ግሎባል_መልስ = 0

    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return (0, 0)
            
            left_count, left_val = dfs(root.left) 
            right_count, right_val = dfs(root.right)
            count, val = left_count + right_count + 1, left_val+ right_val + root.val
            self.ግሎባል_መልስ += abs(count-val)
            return (count, val)
        
        count, val = dfs(root)
        return self.ግሎባል_መልስ - abs(count-val)

        
