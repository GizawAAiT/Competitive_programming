# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        l = head
        for  i in range(left-1):
            l = l.next
        
        vals = [] 
        temp = l
        for i in range(right-left+1):
            vals.append(temp.val)
            temp = temp.next
        
        vals.reverse()
        
        for i in range(right-left+1):
            l.val = vals[i]
            l = l.next
            
        return head