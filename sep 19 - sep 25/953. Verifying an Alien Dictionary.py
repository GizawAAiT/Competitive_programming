class Solution:
    def isAlienSorted(self, w: List[str], pa: str) -> bool:
        if len(w)==1: return True
        d={}
        for i in range(len(pa)):
            d[pa[i]]=i 
        
        def seq(w1,w2):
            i=0
            while i<len(w1) and i<len(w2):
                if d[w1[i]]<d[w2[i]]: return True
                if d[w1[i]]>d[w2[i]]: return False
                i+=1
            return True if not w1[i:] or not(w1[i:] or w2[i:]) else False
        for i in range(1,len(w)):
            if not seq(w[i-1],w[i]): return False
        return True