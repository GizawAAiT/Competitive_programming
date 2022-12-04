class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s, t = list(s), list(t)
        s.sort()
        t.sort()
        
        return s == t