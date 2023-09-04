class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = list(str(n))
        
        P, S = 1, 0
        while n:
            dig = int(n.pop())
            P, S = P*dig, S + dig
        return P-S