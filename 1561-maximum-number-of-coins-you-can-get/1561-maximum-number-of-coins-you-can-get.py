class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        return sum([piles[_] for _ in range(-2, -2-(len(piles)//3)*2, -2)])