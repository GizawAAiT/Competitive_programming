class Solution:
    def kthLargestNumber(self, n, k) -> str:
        
        n=list(map(int,n))
        n=sorted(n,reverse=True)
        return str(n[k-1])