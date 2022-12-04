class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # return 
        s,t=list(s),list(t)
        i=0
        def edit(s):
            i=0
            while i<len(s):
                if s[i]=="#" and i>0: 
                    s.pop(i-1)
                    s.pop(i-1)
                    i-=1
                elif s[i]=="#": s.pop(i)
                else: i+=1
            return s
        return edit(s)==edit(t)