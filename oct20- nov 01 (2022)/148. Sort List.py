# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t = head
        vals = []
        while t:
            vals.append(t.val)
            t = t.next
        vals.sort()
        
        t = head
        while vals:
            t.val = vals[0]
            vals.pop(0)
            t = t.next
        return head