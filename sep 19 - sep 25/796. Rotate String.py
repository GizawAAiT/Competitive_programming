class Solution:
    def rotateString(self, s: str, g: str) -> bool:
        if len(s)!=len(g): return False
        if len(s)==0: return True
        
        s=s+s
        i=0
        while i<len(s)-len(g):
            if s[i:i+len(g)]==g: return True
            i+=1
        return False
        
    