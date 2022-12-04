class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n ==1:
            return 1
        i, j = 0, n
        while i < j-1:
            k = (i+j)//2
            if k**2 + k ==2*n:
                return k
            if k**2 + k < 2*n:
                i = k
            else:
                j = k
        return i