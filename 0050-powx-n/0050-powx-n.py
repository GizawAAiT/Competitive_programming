class Solution:
    def myPow(self, x: float, n: int) -> float: 
        def recursive_pow(x, n):
            if n == 0:
                return 1 
            if n == 1:
                return x
            if n%2:
                return x * recursive_pow( x*x, (n-1)//2)
            return recursive_pow(x*x, n//2)
        return recursive_pow(x, n) if n>0 else 1/recursive_pow(x, -n)
        
        