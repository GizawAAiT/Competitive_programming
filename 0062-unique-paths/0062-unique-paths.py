class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ans = [[0 for i in range(n)] for j in range(m)]
        print(ans)
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    ans[i][j] = 1
                else:
                    ans[i][j] = ans[i-1][j]+ans[i][j-1]
                    
        return ans[-1][-1]