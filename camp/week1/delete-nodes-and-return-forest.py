# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        roots = []
        

        def postOrder(root):
            if not root:
                return False

            left = postOrder(root.left)
            right = postOrder(root.right)
            # paralize left and right if necessary
            if not left:
                root.left = None
            if not right:
                root.right = None  

            l, r = root.left, root.right
            if root.val in to_delete:
                if l : roots.append(l) 
                if r: roots.append(r)  
                
            return root.val not in to_delete

        if root.val not in to_delete:
            roots.append(root)

        postOrder(root)
        return roots


            