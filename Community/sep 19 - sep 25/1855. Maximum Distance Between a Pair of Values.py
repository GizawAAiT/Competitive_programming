class Solution:
    def maxDistance(self, n1: List[int], n2: List[int]) -> int:
        i,j=0,0
        mxdis=0
        while j<len(n2) and i<len(n1):
            if n1[i]<=n2[j]:
                mxdis=max(mxdis,j-i)
                j+=1
            elif j==i: i=j=i+1
            else: i+=1
        return mxdis
                