# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def solve(root):
            if not root:
                return 0
            leftSum = 0 if root.val < low else solve(root.left)
            rightSum = 0 if root.val > high else solve(root.right)
            return root.val * (1 if low <= root.val <= high else 0) + leftSum + rightSum
            # return root.val + self.rangeSumBST(root.left) + self.rangeSumBST(root.right)
        
        return solve(root)