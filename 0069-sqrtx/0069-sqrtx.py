class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 0, x
        
        while low<=high:
            middle = low + (high-low)//2
            if middle **2 == x: return middle
            if middle ** 2 <= x:
                low = middle +1
            else:
                high = middle -1
                
        return high
        