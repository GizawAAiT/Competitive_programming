class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[0]*n for _ in range(m)]
        # print(m,n,dp)
        for i in range(m):
            for j in range(n):
                if i==0 or j==0:
                    dp[i][j]=1 
                    # print("k")
                else:
                    dp[i][j]=dp[i][j-1]+dp[i-1][j]
        # print(dp)
        return dp[m-1][n-1]