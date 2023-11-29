class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping1, mapping2 = {}, {}
        for c1, c2 in zip(s, t):
            if c1 in mapping1 and mapping1[c1] != c2: return False
            mapping1[c1] = c2
            if c2 in mapping2 and mapping2[c2] != c1: return False
            mapping2[c2] = c1
        return True