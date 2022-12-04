class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        d,ans={},[]
        for i in range(len(mat)):
            d[(sum(mat[i]),i)]=i
        ind = sorted(d.keys())
        print(ind)
        for i in range(k):
            ans.append(d[ind[i]])
        return ans
        
        
        