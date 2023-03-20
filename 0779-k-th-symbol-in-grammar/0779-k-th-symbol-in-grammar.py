class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        
        complement = False
        
        def f(n, k):
            nonlocal complement
            if n == 2:
                return [0, 1][k]
            if k >= 2 ** (n-2):
                complement = not complement
            
            k %= 2 **(n-2)
            n -= 1
            print((n,k, complement))
            return f(n, k)
        
        ans = f(n, k-1)
        if complement:
            ans = 0 if ans == 1 else 1
        return ans
        
        