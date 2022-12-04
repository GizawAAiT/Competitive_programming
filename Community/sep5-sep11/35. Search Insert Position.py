
class Solution:
    def searchInsert(self, n: List[int], target: int) -> int:
#         if len(n)==1:
            
        a,b  = 0,len(n)-1
        if target <= n[a]:
            return 0
        if target > n[b]:
            return b+1
        while a<b:
            
            if target == n[(a+b)//2]:
                return (a+b)//2
            elif target < n[(a+b)//2]:
                b = (a+b)//2
            else:
                a = (a+b)//2
            if a == b-1:
                return a+1