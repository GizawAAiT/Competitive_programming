class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        maxLocal = [[0 for _ in range(len(grid[0])-2)] for _ in range(len(grid)-2)]
        
        for a in range(len(grid)-2):
            for b in range(len(grid[0])-2):
                mx = 0
                for i in range(a, a+3):
                    for j in range(b, b+3):
                        mx = max(mx, grid[i][j])
                
                maxLocal[a][b] = mx
        return maxLocal