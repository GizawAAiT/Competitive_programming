class Solution:
    def minTimeToType(self, word: str) -> int:
        positions = [ord(x)-97 for x in word]
        cur = cost = 0
        for pos in positions:
            diff = abs(pos-cur)
            cost += min(diff, 26-diff)
            cur = pos
        
        return cost + len(positions)
