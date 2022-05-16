# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) ->ListNode:
        
        if not head:
            return None
        l=[]
        
        def list(h):
            while h:
                l.append(h.val)
                h=h.next
        list(head)
        
        def frq(l):
            f=[1]
            for i in range(1,len(l)):
                if l[i]==l[i-1]:
                    f[-1]+=1
                else:
                    f.append(1)
            return f
        
        frq = frq(l)
        
        parent = ListNode()
        prev = parent
        prev.next = head
        nxt = head
    
        for i in range(len(frq)):
            if frq[i]==1:
                prev.next=nxt
                prev=prev.next
                nxt=nxt.next
            else:
                for i in range(frq[i]):
                    nxt=nxt.next
            
                
        prev.next=nxt   
        return parent.next
                
                
                