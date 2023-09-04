class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        trans = [[g[i] for g in grid] for i in range(len(grid[0]))]
        
        equals = 0
        for g in grid:
            for t in trans:
                if g == t: equals += 1
        return equals