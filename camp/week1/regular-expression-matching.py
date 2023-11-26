class Solution:
    def isMatch(self, s: str, pattern: str) -> bool:
        def match(a, b):
            return '.' in (a,b) or a == b

        pat = []
        for p in pattern:
            if p == '*':
                pat.append((pat.pop()[0], float('inf')))
            else: pat.append((p, 1))
        
        @cache
        def backtrack(sIndx, pIndx):
            if sIndx >= len(s) and pIndx >= len(pat): return True

            if sIndx >= len(s):
                for pI in range(pIndx, len(pat)):
                    if pat[pI][1] == 1: return False
                return True

            if pIndx >= len(pat):
                return False
                
            if pat[pIndx][1] == float('inf'):
                return backtrack(sIndx, pIndx +1) or match(s[sIndx], pat[pIndx][0]) and backtrack(sIndx +1, pIndx)
            
            return match(s[sIndx], pat[pIndx][0]) and backtrack(sIndx +1, pIndx+1)
        
        return backtrack(0, 0)



                
