class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high - low + 1) // 2 + (high % 2 and low % 2)
