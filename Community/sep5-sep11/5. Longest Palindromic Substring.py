class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)==1:
            return s
        pal = s[0]
        
        for i in range(len(s)):
            a = i
            b = i
            
            while a>-1 and b < len(s):
                if s[a]!=s[b]:
                    break
                a-=1
                b+=1
            if b-1-a > len(pal):
                pal = s[a+1:b]
            
            
            c = i
            d = i+1 
            
            while c>-1 and d < len(s):
                if s[c]!=s[d]:
                    break
                c-=1
                d+=1
            if d-1-c > len(pal):
                pal = s[c+1:d]
        return pal