# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next : return head
        n = 0
        t = head
        while t: 
            n += 1
            t = t.next
            
        
        k %= n
        if k == 0: return head
        left = right = head
        while k:
            k -= 1
            right = right.next
        
        while right.next:
            right = right.next
            left = left.next
        
        temp = left.next 
        right.next = head 
        left.next = None
        return temp 
        