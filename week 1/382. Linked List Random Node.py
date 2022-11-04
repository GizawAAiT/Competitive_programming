# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        
        self.head = head
    def getRandom(self) -> int:
        N = self.size()-1
        n = random.randint(0,N)
        t = self.head
        while n>0:
            n-=1
            t = t.next
        return t.val if t else self.head.val
    def size(self):
        t, s = self.head, 0
        while t:
            s+=1
            t=t.next
        return s
    
        
            


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()