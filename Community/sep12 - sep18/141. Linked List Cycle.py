# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        catche = set()
        p = head
        while p:
            if p in catche:
                return True
            catche.add(p)
            p = p.next
        
        return False