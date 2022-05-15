# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        parent = ListNode()
        
       
        self.prev = parent
        self.prev.next=head
        self.front = head
        
        def len(h):
            l=0
            while h:
                l+=1
                h=h.next
            return l
        
        
        def nodeCut():
            t1 = self.prev.next
            t2 = self.front.next
            self.prev.next=t2
            
            self.front.next=self.front.next.next 
            self.prev.next.next = t1 
                       
        
  
        for i in range(len(head)//k):
            for j in range(k-1):
                nodeCut()
            self.prev = self.front
            self.front = self.front.next
            
        return parent.next
                
                