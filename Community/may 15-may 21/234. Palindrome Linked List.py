# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        def iter (h):
            l=[]
            while h:
                l.append(h.val)
                h=h.next
            return l
        nodes =iter(head)
        
        p=0
        q=len(nodes)-1
        while p<q:
            if nodes[p]!=nodes[q]:
                
                return False
            p+=1
            q-=1
        return True