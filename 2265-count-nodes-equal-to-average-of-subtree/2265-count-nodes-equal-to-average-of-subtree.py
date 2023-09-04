# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count = 0
        
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def sumAndCount(root):
            if not root:
                return (0, 0)
            left = sumAndCount(root.left)
            right = sumAndCount(root.right)
            node = (left[0]+right[0]+root.val, left[1]+right[1]+1)
            if node[0]//node[1] == root.val:
                self.count += 1
            return node
        sumAndCount(root)
        return self.count