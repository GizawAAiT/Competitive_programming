class Solution:
    def getHint(self, s: str, g: str) -> str:
        s,g=list(s),list(g)
        A=B=0
        
        i=0
        while i<len(s):
            if s[i]==g[i]:
                A+=1
                s.pop(i)
                g.pop(i)
            else:i+=1
        i = 0
        while i<len(s):
            if g[i] in set(s):
                B+=1
                s.remove(g[i]) 
                g.pop(i)
                 
            else: i+=1
        return f"""{A}A{B}B"""
        