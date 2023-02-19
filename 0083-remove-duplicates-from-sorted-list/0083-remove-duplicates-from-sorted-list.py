# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head):
        temp = head
        while temp:
            while temp and temp.next and temp.next.val == temp.val:
                temp.next = temp.next.next
            temp = temp.next 
        return head