# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        
        def length(h):
            l=0
            while h:
                h=h.next
                l+=1
            return l
          
        if not head.next:
            return
        def rev (h):
            
            leng= length(h) 
            t2=h.next
            h.next=None
            t=None
            for i in range(leng-1):
                t=h
                h=t2
                
                t2=t2.next
                h.next=t
                
            return h
        def iter(h):    
            l=[]
            while h:
                l.append(h.val)
                h=h.next
            return l
        duma=ListNode()
        slow = fast = duma
        slow.next=head
        fast.next=head
        while fast and fast.next:  
            slow=slow.next
            fast=fast.next.next

        tempo=slow.next
        slow.next=None
        tempo=rev(tempo)
        slow.next=tempo
        p=head
        for i in range(((length(head)+1)//2)-1):
            
            tr=slow.next
            tr2=p.next
            slow.next=slow.next.next
            p.next=tr
            tr.next=tr2
            p=p.next.next
        
                
                