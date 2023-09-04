# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root):
        def tilt(root):
            # global res
            if not root:
                return 0, 0
            l, l_res = tilt(root.left)
            r, r_res = tilt(root.right)
            return l+r+root.val, l_res+r_res+abs(l-r)

        return tilt(root)[1]

        
        