# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
#         recursive
        # return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
    
    
#     iterative
        Q = [root]
        ans = []
        
        while Q:
            node = Q.pop(0) 
            ans.append(node.val) 
            if node.right:
                Q.insert(0,node.right)
            if node.left:
                Q.insert(0,node.left) 
        return ans
            
                             