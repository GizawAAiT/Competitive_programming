class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        

        
        q = dividend/divisor
        if q > 2**31 -1:
            return 2**31 -1
        if q < -2**31 :
            return -2**31 
        if q == dividend//divisor:
            return int(q)
        if q <0:
            return ceil(q)
        else:
            return floor(q)