# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        t = root
        setP = set()
        while t:

            setP.add(t)
            if t == p:
                break
            if t.val < p.val:
                t = t.right
            else:
                t = t.left
                
        t = root
        res = root
        while t!=q:
            if t in setP:
                res = t
                print(t.val)
            if t == q:
                break
            if t.val < q.val:
                t = t.right
            else:
                t = t.left
        return q if q in setP else res
            