class Solution:
    def getSum(self, a: int, b: int) -> int:
        sign = 1 if b > 0 else -1
        print(sign)
        for i in range(abs(b)):
                a +=sign*1
        
        return a