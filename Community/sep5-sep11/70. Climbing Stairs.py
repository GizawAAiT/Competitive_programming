class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        Dp = [1,2]
        
        i = 2
        while i < n: 
            Dp.append(Dp[-1]+Dp[-2]) 
            i+=1
        return Dp[-1]