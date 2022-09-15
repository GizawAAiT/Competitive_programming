class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
             return 10
        c = [9*9]
        for i in range(n-2):
            c.append(c[-1]*(8-i))
        return 10 + sum(c)
            
