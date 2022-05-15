# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) ->ListNode:
        if not head:
            return None
        cancler = head
        while cancler.next:
            if cancler.val == cancler.next.val:
                cancler.next=cancler.next.next
            else:
                cancler=cancler.next
        return head
                
                
                