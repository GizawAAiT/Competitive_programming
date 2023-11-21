class Solution:
    def soupServings(self, n: int) -> float:
        @cache
        def recur(i, j):
            if i <= 0 and j <= 0: return .5
            if i <= 0: return 1
            if j <= 0: return 0
            return .25 * (recur(i-4,j) + recur(i-3,j-1) + recur(i-2, j-2) + recur(i-1, j-3))
        n = ceil(n/25) 
        return 1 if n > 180 else recur(n, n)
       