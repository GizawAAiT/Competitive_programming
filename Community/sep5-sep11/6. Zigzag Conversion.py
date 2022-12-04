class Solution:
    def convert(self, s: str, n: int) -> str:
        if n == 1:
            return s
        new = ""
        
        for i in range(n):
            t = i
            
            while t<len(s):
                new = new + s[t]
                if i not in [0,n-1] and t+2*(n-i)-2 < len(s):
                    new = new + s[t+2*(n-i)-2] 
                t+=2*(n-1)
        return new