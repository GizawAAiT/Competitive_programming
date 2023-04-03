# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head) :
        greater = {}
        stack, p = [head], head
        while p.next:
            p = p.next
            while stack and p.val > stack[-1].val:
                greater[stack[-1]] = p.val
                stack.pop()
            stack.append(p)
        for node in stack: greater[node] = 0
        
        res = []
        print(res)
        while head:
            res.append(greater[head])
            head = head.next
        return res