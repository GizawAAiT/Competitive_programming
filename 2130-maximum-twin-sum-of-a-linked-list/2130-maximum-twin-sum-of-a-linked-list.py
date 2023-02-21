# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        half = []
        fast, slow = head.next, head
        while fast and fast.next:
            half.append(slow.val)
            slow=slow.next
            fast=fast.next.next
        half.append(slow.val)
        
        # print(half,slow.val,fast.val)
        j = len(half)-1
        slow=slow.next
        max_sum = 0
        
        while slow:
            max_sum = max(max_sum, slow.val+half[j])
            j -=1
            slow=slow.next
        return max_sum
    
        
            