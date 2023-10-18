# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def __init__(self):
    #     self.answer = 0

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inOrder(root, vals):
            if len(vals) >= k:
                return

            if not root:
                return 0
            
            inOrder(root.left, vals)
            vals.append(root.val)
            inOrder(root.right, vals)

        vals = []
        inOrder(root, vals)
        return vals[k-1]


