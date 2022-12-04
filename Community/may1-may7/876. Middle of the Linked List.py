# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        middle_pointer=end_pointer=head
        while end_pointer and end_pointer.next:
            middle_pointer=middle_pointer.next
            end_pointer=end_pointer.next.next
        return middle_pointer