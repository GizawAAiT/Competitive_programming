# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        while lists:
            t = lists.pop()
            while t:
                nodes.append(t.val)
                t = t.next
        nodes.sort()
        
        t = dummy = ListNode()
        while nodes:
            n = ListNode(nodes.pop(0))
            t.next = n
            t = t.next
        return dummy.next
            