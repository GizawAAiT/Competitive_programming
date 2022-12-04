class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        if n==1: return True
        prev,n=n%2,n//2
        
        while n>1:
            if n%2 == prev: return False
            prev,n=n%2,n//2
        return False if n==prev else True