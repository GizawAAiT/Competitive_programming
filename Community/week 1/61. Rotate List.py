# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0: return head
        def size(h):
            t, size = h, 0
            while t :
                t = t.next
                size += 1
            return size
                
        k = size(head) - (k % size(head))
        if k == size(head): return head
        t = head
        while k>1:
            k-=1
            head=head.next
        t2 = head.next
        # print(t2.val) 
        head.next = None
        head = t2
        while t2 and  t2.next:
            print(t2.val,"inside the loop")
            t2=t2.next
        t2.next = t  
        return head      
                             
             
                
                