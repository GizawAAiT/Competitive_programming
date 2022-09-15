class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        s = sorted(list(s))
        
        n = 0
        i = len(s) -1
        while i > 0:
            if s[i] == s[i-1]: 
                n+=2
                i-=2
            else:
                i-=1
        return n+1 if len(s)>n else n
            
            
            
            
        