# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next: return head
        o, e = head, head.next
        ans = t1 = odd = ListNode()
        
        while o:
            n = ListNode(o.val)
            t1.next = n
            t1=t1.next
            if o.next and o.next.next: 
                o=o.next.next
            else: break
        
        begin = t = even = ListNode()
        while e : 
            n = ListNode(e.val)
            t.next = n
            t=t.next
            if e.next and e.next.next: 
                e=e.next.next
            else: break
        t1.next = begin.next
        return ans.next