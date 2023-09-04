# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
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
        mxsum=0
        while p<q:
            mxsum=max(mxsum,nodes[p]+nodes[q])
            p+=1
            q-=1
        return mxsum