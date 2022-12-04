class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        a,b = 0,x
        while a<b-1:
            m = ((a+b)//2)
            if m * m < x:
                a = m
            elif m * m == x:
                return m
            else:
                b = m
        return a