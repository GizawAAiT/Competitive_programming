class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ln = [len(s) for s in strs]
        short = min(ln)
        p = 0
        stop = False
        
        while p < short and short:
            
            t = strs[0][p] 
            for st in strs:
                if st[p] != t:
                    stop = True
                    break
            if stop == True:
                break
            p+=1
            
        return strs[0][0:p]
                