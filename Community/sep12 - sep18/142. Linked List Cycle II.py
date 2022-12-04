# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        catche = set()
        t = head
        while t :
            if t in catche:
                return t
            catche.add(t)
            t = t.next
        return None
                