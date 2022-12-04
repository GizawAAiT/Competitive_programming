# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        a,b = 1, n
        if isBadVersion(a):
            return a
        while a<b-1:
            m = (a+b)//2
            
            if not isBadVersion(m):
                a = m
            else:
                b = m
        #number limit (int range)
        if b > 2**31-1:
            return 2*31-1
        if b < -2**31:
            return -2**31

        return b