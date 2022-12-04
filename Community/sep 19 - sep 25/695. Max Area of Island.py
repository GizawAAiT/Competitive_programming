class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        
        def Area(i,j):
            A = 0
            if i>=R or i<0 or j>=C or j<0: 
                return 0            
            if grid[i][j]==0:                
                return 0            
            else:
                grid[i][j] = 0
                A+=1
                return A + Area(i+1,j)+Area(i-1,j)+Area(i,j+1)+Area(i,j-1)
            
            
            
        A = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] ==1:
                    A = max(A,Area(i,j))
        return A