# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head):
        index = 1
        pointer = head
        pe =even = ListNode()
        po = odd = ListNode()
        while pointer:
            if index%2==1:
                po.next=ListNode(pointer.val)
                po = po.next
            else:
                pe.next=ListNode(pointer.val)
                pe = pe.next
            pointer = pointer.next
            index +=1
        even = even.next
        po.next=even
        return odd.next
   