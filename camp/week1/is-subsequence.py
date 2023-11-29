class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p = 0
        for char in s:
            while p < len(t) and char != t[p]: p += 1

            if p >= len(t): return False
            p += 1
        return True 

