# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        sampleNode = ListNode(0,head)
        l_pointer = sampleNode
        r_pointer = head
        
        while n :
            r_pointer= r_pointer.next
            n-=1
        while r_pointer :
            r_pointer= r_pointer.next
            l_pointer = l_pointer.next
        
        l_pointer.next = l_pointer.next.next
        return sampleNode.next