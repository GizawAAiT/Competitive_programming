class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        f={s[0]:1} 
        i,j=0,0
        res=1
        while j<len(s):
            while (j-i+1) - max(f.values()) >k:
                f[s[i]]-=1
                i+=1
            res=max(res,(j-i+1))
            if j<len(s)-1:
                j+=1
                f[s[j]]=f[s[j]]+1 if s[j] in f.keys() else 1
            else:
                break
        res=max(res,j-i+1)
        return res
            
            