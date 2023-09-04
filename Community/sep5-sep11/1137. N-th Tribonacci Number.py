class Solution:
    def tribonacci(self, n: int) -> int:
        memo = [-1 for _ in range(n+1)]
        return self.T_Rec(memo,n)
    def T_Rec(self,memo,n):
        if n < 3:
            return int(n>0)
        if memo[n] > -1:
            return memo[n]
        memo[n] = self.T_Rec(memo,n-1) + self.T_Rec(memo,n-2) + self.T_Rec(memo,n-3)
        return memo[n]