class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        row_size = len(dungeon)
        col_size = len(dungeon[0])

        dp = [[0]* col_size for _ in range(row_size)] 
        for i in range(row_size-1, -1, -1):
            for j in range(col_size-1, -1, -1):
                if i == row_size-1 and j == col_size-1:
                    dp[i][j] = max(1, 1-dungeon[i][j])
                elif i == row_size-1:
                    dp[i][j] = max(1, dp[i][j+1]-dungeon[i][j]) 
                elif j == col_size-1:
                    dp[i][j] = max(1, dp[i+1][j]-dungeon[i][j])
                else:
                    dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1])-dungeon[i][j])
        
        return dp[0][0]

        