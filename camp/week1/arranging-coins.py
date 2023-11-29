class Solution:
    def arrangeCoins(self, n: int) -> int:
        k = 0
        while n > 0:
            n -= k+1
            k += 1
        return k if n == 0 else k - 1