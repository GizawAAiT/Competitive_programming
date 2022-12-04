class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-i for i in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            s1 = heapq.heappop(stones)
            s2 = heapq.heappop(stones)
            heapq.heappush(stones, - abs(s1-s2))
        return -stones[0] if stones else 0