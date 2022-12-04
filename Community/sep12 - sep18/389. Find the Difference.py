class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = sorted(list(s))
        t = sorted(list(t))
        for i in range(len(s)): 
            if s[i]!=t[i]:
                return t[i]
        return t[-1]