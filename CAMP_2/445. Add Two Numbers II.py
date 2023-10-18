# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def printList(l):
            while l:
                print(l.val,'-->', end = '')
                l = l.next
            print()

        def reversedList(l):
            prev = None
            while l:
                t = l.next
                l.next = prev
                prev = l
                l = t

            return prev
        # printList(l1)
        l1, l2 = reversedList(l1), reversedList(l2)
        # printList(l1)
        answer_root = l1
        carry = 0
        while l2 or carry>0:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0 
            cur_sum = v1 + v2 + carry
            carry = cur_sum //10
            cur_sum %= 10
            l1.val = cur_sum
            if l2:
                l2 = l2.next
            
            if not l1.next and (l2 or carry):
                l1.next = ListNode(0)
            l1 = l1.next

        return reversedList(answer_root)

