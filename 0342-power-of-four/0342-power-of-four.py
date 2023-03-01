class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 0: 
            return False
        
        def recur(n):
            if n<4:
                return n == 1
            return recur(n/4)
        
        return recur(n)
    