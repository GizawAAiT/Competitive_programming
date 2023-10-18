class Solution:
    def myPow(self, x: float, n: int) -> float: 
        def dfs(x, n):
            if  n <2:
                return pow(x, n)
            if n%2:
                return x * dfs( x*x, (n-1)//2)
            return dfs(x*x, n//2)
        return dfs(x, n) if n>0 else 1/dfs(x, -n)
        
        