# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        dummy.next = head
        
        while cur and cur.next and cur.next.next:
            if cur.next.val==cur.next.next.val:
                t = cur.next
                while t and t.next and t.val==t.next.val:
                    t = t.next
                cur.next=t.next
            else: cur = cur.next
        return dummy.next
    