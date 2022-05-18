# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        n=[]
        print(len(n))
        
        for i in lists:
            while i:
                n.append(i.val)
                i=i.next
        n=sorted(n)
        if len(n)==0:
            return 
        parent=ListNode(n[0],None) 
        
        head = parent
        for i in n:
            nd = ListNode(i,None)
            head.next=nd
            head=head.next
            
        parent=parent.next
       
        return parent