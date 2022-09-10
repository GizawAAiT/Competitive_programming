# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2        
        if not list2 or not list1 and not list2:
            return list1        
        
        while list2 and list2.val <= list1.val:
            t = list1
            list1 = list2
            list2=list2.next
            list1.next = t         
        
        t = list1            
        while t.next and list2:            
            if list2.val <= t.next.val:
                super_tempo = t.next
                t.next = list2
                t = t.next
                list2 = list2.next
                t.next = super_tempo
            else:
                t = t.next
                
        if list2:
            t.next = list2
        return list1
                