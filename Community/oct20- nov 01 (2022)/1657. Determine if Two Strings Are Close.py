class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        w1, w2 = {}, {}
        for w in word1:
            if w in w1.keys():
                w1[w]+=1
            else: w1[w] = 1
        for w in word2:
            if w in w2.keys():
                w2[w]+=1
            else: w2[w] = 1
        v1, v2 = (list(w1.values()),list(w2.values()))
        k1, k2 = list(w1.keys()), list(w2.keys())
        v1.sort()  
        v2.sort()
        k1.sort()
        k2.sort()
        return v1 == v2 and k1==k2