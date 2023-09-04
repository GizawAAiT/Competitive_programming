# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], target: int) -> Optional[ListNode]:
        t = dummy = ListNode()
        dummy.next = head
        l = largers = ListNode()
        
        while t.next: 
            if t.next.val >= target:
                l.next = ListNode(t.next.val)
                t.next = t.next.next
                l = l.next
                
            else:
                t = t.next
                
        t.next = largers.next
        return dummy.next