class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        count = 0
        P = set()
        Q = set()
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count+=1
                Q.add(s1[i]) 
                P.add(s2[i])
                
        return (count ==2 and P == Q) or count == 0 
