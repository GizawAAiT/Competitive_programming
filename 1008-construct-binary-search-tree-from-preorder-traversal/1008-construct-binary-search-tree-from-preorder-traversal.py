# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        
        stack = [root]
        for n in preorder[1:]:
            
            if n < stack[-1].val:
                stack[-1].left = TreeNode(n)
                stack.append(stack[-1].left)
            
            else:
                
                while stack and stack[-1].val < n:
                    parent = stack.pop()
                
                parent.right = TreeNode(n)
                stack.append(parent.right)
                
        return root