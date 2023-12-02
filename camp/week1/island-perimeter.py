class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        def inBound(i, j):
            return 0<=i<row and 0<=j<col
        def directions(r, c):
            return [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
            
        res = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c]:
                    for newR, newC in directions(r, c):
                        res += not inBound(newR, newC) or not grid[newR][newC]
        
        return res