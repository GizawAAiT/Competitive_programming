class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # p = []
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         p.append((i,j))
        
        R, C = len(grid), len(grid[0])
                
        def land(i,j):
            if i>=R or i<0 or j>=C or j<0: 
                return             
            if grid[i][j]=="0":                
                return 
            grid[i][j] = "0"            
            land(i+1,j)
            land(i-1,j)
            land(i,j+1)
            land(i,j-1)
        ans = 0   
        for i in range(R):
            for j in range(C):
                if grid[i][j] =="1":
                    ans+=1
                    land(i,j)
        return ans