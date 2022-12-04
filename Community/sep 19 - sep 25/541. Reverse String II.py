class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # s=list(s)
        i=0
        while i<len(s):
            t=s[i:i+k] if i+k<=len(s) else  s[i:]
            
            t="".join(list(reversed(t)))
            s=s[:i]+t+s[i+k:] if i+k<=len(s) else s[:i]+t
            i+=2*k
        return s
            