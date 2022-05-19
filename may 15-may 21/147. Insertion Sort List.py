# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        st=[]
        while head:
            st.append(head.val)
            head=head.next
        
        
        st=sorted(st)
        
        head = ListNode()
        temp=head
        head = temp
        for i in st:
            p=ListNode()
            p.val = i
            
            temp.next=p
            temp=temp.next
        head=head.next
        return head
        