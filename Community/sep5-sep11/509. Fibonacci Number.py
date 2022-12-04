class Solution:
    def fib(self, n: int) -> int:
        memo = [-1 for _ in range(n+1)]
        return self.fRecursive(memo,n)
        # print(memo,len(memo))
        
    def fRecursive(self,memo,n):
        if n<2:
            return n
        if memo[n]>-1:
            return memo[n]
        memo[n] = self.fRecursive(memo,n-1)+ self.fRecursive(memo,n-2)  
        return memo[n]