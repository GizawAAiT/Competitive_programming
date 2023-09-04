class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        def helper(i,j):
            return grid[i][j] + sum(grid[i-1][j-1:j+2]) + sum(grid[i+1][j-1:j+2])
        res = 0
        for i in range(1,len(grid)-1):
            for j in range(1,len(grid[0])-1):
                res = max(res, helper(i,j))
        return res
        