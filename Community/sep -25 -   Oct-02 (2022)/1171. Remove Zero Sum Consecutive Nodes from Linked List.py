# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, h: Optional[ListNode]) -> Optional[ListNode]:
        array = []
        while h:
            array.append(h.val)
            h = h.next        
        
        i = 0
        while i<len(array):
            j, curSum =i+1, array[i]
            while j<len(array):                
                if curSum == 0: 
                    for _ in range(j-i):
                        array.pop(i)                    
                    j, curSum=i+1, array[i]
                else: 
                    curSum += array[j] 
                    j+=1
            if curSum == 0: 
                for _ in range(j-i):
                    array.pop(i)  
            i+=1

        t = head = ListNode()
        for n in array:
            node = ListNode(n)
            t.next = node
            t = t.next
        return head.next
            
        