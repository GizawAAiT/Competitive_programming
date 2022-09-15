# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        
        
        
        def backtrack(root,target):
            parent = {root:None}
            Q = [root]
            while Q:
                node = Q.pop(0)
                if node == target:
                    break
                if node.left:
                    parent[node.left] = node
                    Q.append(node.left)
                if node.right:
                    parent[node.right] = node
                    Q.append(node.right)
            
            path = [target]
            while parent[path[-1]]:
                path.append(parent[path[-1]])
            return list(reversed(path))
        pathp , pathq = backtrack(root,p), backtrack(root,q)
        i = 0
        while i < len(pathp) and i < len(pathq) and pathp[i]==pathq[i]:  
            i+=1
        return pathp[i-1]
      
            
            
        