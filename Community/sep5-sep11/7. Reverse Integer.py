class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x<0:
            sign = -1
        
        x=x*sign
        strn = str(x)
        x = "".join(strn[i] for i in range(len(strn)-1,-1,-1))
        x = int(x)*sign
        if x < -2**31 or x>2**31-1:
            x=0            
        return x