# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next = None, prev = None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        
        def bst(i, j):
            if i > j: return None
            mid = (i+j)//2
            return TreeNode(vals[mid], bst(i, mid-1), bst(mid+1, j))
        
        return bst(0, len(vals)-1)



        
