# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        l = head
        for  _ in range(left-1):
            l = l.next
        vals = []
        temp = l
        for _ in range(right-left+1):
            vals.append(temp.val)
            temp = temp.next
        vals.reverse()
        for _ in range(right-left+1):
            l.val = vals[_]
            l = l.next
        return head