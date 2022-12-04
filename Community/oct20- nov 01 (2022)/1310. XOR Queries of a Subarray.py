class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        
        pref_XOR = [arr[0]]
        for i in range(1,len(arr)):
            pref_XOR.append(pref_XOR[-1]^arr[i]) 
        
        res = []
        for i, j in queries:
            res.append(pref_XOR[j] if i ==0 else pref_XOR[j]^pref_XOR[i-1])
        return res