class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEat(v):
            return sum([ceil(p/v) for p in piles])<=h
        low, high = 0, max(piles)+1
        while low<high-1: 
            mid = low + (high-low)//2
            if canEat(mid):
                high = mid
            else:
                low = mid
        return high