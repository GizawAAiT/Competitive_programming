class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @cache
        def backtrack(i, j, k):
            # print(i, j, k)
            if k >= len(s3):
                return i >= len(s1) and j >= len(s2)

            c1, c2 = s1[i] if i<len(s1) else None, s2[j] if j<len(s2) else None

            if s3[k] not in (c1, c2): return False
            if c1 == s3[k] and c2 == s3[k]:
                return backtrack(i+1, j, k+1) or backtrack(i, j+1, k+1)
            
            return backtrack(i+1, j, k+1) if c1 == s3[k] else backtrack(i, j+1, k+1)
        
        return backtrack(0, 0, 0)
