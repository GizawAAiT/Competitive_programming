class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s = list(reversed(list(s)))
        j = 0
        
        while s:
            while j<len(t) and s[-1]!=t[j]: 
                j+=1 
            
            if j>=len(t): break
            else:
                j+=1
                s.pop()
        return not s