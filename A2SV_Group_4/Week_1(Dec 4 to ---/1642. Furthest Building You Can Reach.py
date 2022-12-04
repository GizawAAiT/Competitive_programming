class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        climbs = []
        for i in range(len(heights)-1):
            c = heights[i+1] - heights[i]
            if c > 0:
                heapq.heappush(climbs, c)
            if ladders < len(climbs):
                bricks -= heapq.heappop(climbs) 
            if bricks < 0: return i
        return len(heights)-1