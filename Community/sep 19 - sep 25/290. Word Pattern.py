class Solution:
    def wordPattern(self, p: str, s: str) -> bool:
        p,w=list(p),s.split(" ")
        if len(w)!=len(p):return False
            
        print(p,w)
        d={}
        i = 0
        while i<len(p):
            if p[i] in d.keys() and d[p[i]]!=w[i] or w[i] in d.values() and p[i] not in d.keys(): 
                return False            
            else:
                d[p[i]] = w[i]
                i+=1
        return True
