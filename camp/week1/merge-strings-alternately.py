class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1,w2=list(word1),list(word2) 
        mixed=[]
        while w1 and w2:
            mixed.append(w1.pop(0))
            mixed.append(w2.pop(0))
        if w1: mixed.extend(w1)
        if w2: mixed.extend(w2)
        return "".join(mixed)