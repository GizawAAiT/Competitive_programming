# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        mat = [[-1 for _ in range(n)] for _ in range(m)]
        
        left = top = 0
        right = len(mat[0])
        bottom = len(mat)
        
        
        while head:
            #top
            for j in range(left, right):
                mat[top][j]  = head.val
                head=head.next
                if not head: return mat
            #right
            for i in range(top+1, bottom):
                mat[i][right-1] = head.val
                head=head.next
                if not head: return mat
            #bottom
            for j in range(right-2, left-1,-1):
                
                mat[bottom-1][j] = head.val
                head=head.next
                if not head: return mat
            #left
            for i in range(bottom-2, top,-1):
                
                mat[i][left] = head.val
                head=head.next
                if not head: return mat
            top +=1
            left +=1
            right -=1
            bottom -=1
        