class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s): return []
        pf =[0]*26
        for i in range(len(p)):
            pf[ord(p[i])-ord("a")]+=1
        # print(pf)
        
        sf=[0]*26
        for i in range(len(p)):
            sf[ord(s[i])-ord("a")]+=1
        i,j=0,len(p)
        res=[]
        while j<len(s):
            if sf==pf: res.append(i)
            
            sf[ord(s[i])-ord("a")]-=1
            sf[ord(s[j])-ord("a")]+=1
            # print(sf,pf,"\n\n")
            i,j=i+1,j+1
        if sf==pf: res.append(i)
        return res