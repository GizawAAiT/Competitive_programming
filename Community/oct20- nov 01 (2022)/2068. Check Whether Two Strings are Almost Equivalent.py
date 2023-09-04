class Solution:
    def checkAlmostEquivalent(self, w1: str, w2: str) -> bool:
        
        d1, d2 = {}, {}
        
        for w in w1:
            if w in d1.keys():
                d1[w] += 1
            else: d1[w] = 1
        
        for w in w2:
            if w in d2.keys():
                d2[w] += 1
            else: d2[w] = 1
        for w in d1.keys():
            if w not in d2.keys() and d1[w]>3 or w in d2.keys() and  abs(d1[w]-d2[w])>3:
                return False 
            if w in d2.keys(): del d2[w] 
        for w in d2.keys():
            if w not in d1.keys() and d2[w]>3 or w in d1.keys() and  abs(d1[w]-d2[w])>3:
                return False 
        return True