# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()
        mixed = dummy
        
        while list1 and list2  :
          
            if list1.val <=list2.val:
                mixed.next = list1
                list1=list1.next
            else :
                mixed.next = list2
                list2 = list2.next
            mixed = mixed.next
        if list1:
            mixed.next=list1
        if list2:
            mixed.next=list2
        return dummy.next
                
                