# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(root):
            res = []
            if root:
                res += inorder(root.left)
                res.append(root.val)
                res += inorder(root.right)
            return res
        return inorder(root)[k-1]