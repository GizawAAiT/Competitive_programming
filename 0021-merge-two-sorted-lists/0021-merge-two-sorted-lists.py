# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, head1, head2):
        t = head = ListNode()
        def mergeRecursive(head1, head2,t):
            # base case
            if not head1:
                t.next = head2
                t = t.next
                return 
            if not head2:
                t.next = head1
                t=t.next
                return
            
            if head1.val <= head2.val:
                t.next = ListNode(head1.val) 
                t=t.next
                head1 = head1.next
            else:
                t.next = ListNode(head2.val)
                t=t.next
                head2 = head2.next
            
            return mergeRecursive(head1, head2,t)
        mergeRecursive(head1, head2,t)
        return head.next
        
        
#         dummy = ListNode()
#         t = dummy
#         while head1 and head2:
#             if head1.val <= head2.val:
#                 node = ListNode(head1.val) 
#                 t.next = node
#                 head1 = head1.next
#             else:
#                 node = ListNode(head2.val)
#                 t.next = node
#                 head2 = head2.next
#             t= t.next
#         if  head1:
#             t.next = head1
#         if head2:
#             t.next = head2
#         return dummy.next
        