class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row, col = len(heights), len(heights[0])
        def inBound(i, j):
            return 0<=i<row and 0<=j<col
        
        h = [(0, 0, 0)] #effort, row, col.
        visited, max_effort = set([(0, 0)]), 0
        while h:
            eff, r, c = heappop(h)
            max_effort = max(max_effort, eff)
            visited.add((r, c))
            if (r, c) == (row-1, col-1):
                return max_effort
            
            for newR, newC in [(r+1, c), (r, c+1), (r-1, c), (r, c-1)]:
                if inBound(newR, newC) and (newR, newC) not in visited:
                    heappush(h, (abs(heights[newR][newC] - heights[r][c]), newR, newC))
        
        






