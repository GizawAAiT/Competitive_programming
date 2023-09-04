# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
            
        dummy = cur = ListNode(float('-inf'))
        dummy.next = head
        
        while cur and cur.next:
            
            node = cur.next
            cur.next = cur.next.next
            p = dummy
            while p != cur and p.next.val < node.val:
                p = p.next
            
            t = p.next
            p.next = node
            node.next = t
            
            if p == cur:
                cur = cur.next
        return dummy.next
    

        