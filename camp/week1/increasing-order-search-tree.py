# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        stack, a, curr, prev = [], [], root, None
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.right
            curr = stack.pop()
            a.append(curr.val)
            new = TreeNode(curr.val)
            new.right = prev
            prev = new
            curr = curr.left
        return prev
        