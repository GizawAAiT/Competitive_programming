# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        Ans = ListNode()
        cur_pos = Ans
        
        shift = 0
        while l1 or l2 :
            val1= l1.val if l1 else 0
            val2= l2.val if l2 else 0
            
            val = shift + val1 + val2
            shift = val // 10
            val = val % 10
            cur_pos.next = ListNode(val)
            
            cur_pos =cur_pos.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if shift != 0: 
            val = shift
            cur_pos.next = ListNode(val)
            
            cur_pos =cur_pos.next
        Ans =Ans.next
        return Ans