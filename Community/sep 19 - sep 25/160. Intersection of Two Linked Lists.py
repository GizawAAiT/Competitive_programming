# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, hA:ListNode, hB:ListNode):
        t=hA
        catche=set()
        while t:
            catche.add(t)
            t=t.next
        r=hB
        while r:
            if r in catche:return r
            r=r.next
        return None
                
            