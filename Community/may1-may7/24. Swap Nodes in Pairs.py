# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        parent = ListNode(0,head)
        p1,p2=parent,head
        
        while p2 and p2.next:
            nxtset = p2.next.next
            frontier = p2.next
            
            frontier.next=p2
            p2.next=nxtset
            p1.next = frontier
            
            p1=p2
            p2=nxtset
        return parent.next
            
        