class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        last_bit = n & 1
        n >>= 1
        
        while n:
            if last_bit == n & 1: return False
            last_bit = n & 1
            n >>= 1
        
        return True
    