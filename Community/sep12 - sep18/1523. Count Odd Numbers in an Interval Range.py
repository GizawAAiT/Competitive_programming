class Solution:
    def countOdds(self, low: int, high: int) -> int:
        A = 0
        if low%2:
            low +=1
            A +=1
        return A + (high-low+1)//2