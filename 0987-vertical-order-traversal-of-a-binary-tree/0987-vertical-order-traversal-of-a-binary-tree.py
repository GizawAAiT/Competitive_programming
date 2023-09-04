# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic = defaultdict(list)
        def vertical(root, col, row):
            if not root:
                return 
            dic[col].append((root.val, row))
            vertical(root.left, col-1, row+1)
            vertical(root.right, col+1, row+1)
        vertical(root, 0, 0)
        res = []
        
        for key in sorted(dic.keys()):
            dic[key].sort()
            dic[key].sort(key = lambda x:x[1])
            res.append([t[0] for t in dic[key]])
        return res
    