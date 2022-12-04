class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        mat = [[0 for i in range(n)] for j in range(n)]
        
        # print(mat)
        val = 1       
        for i in range(n//2):           
            for m in range(i,n-i): 
                mat[i][m] = val
                val +=1
            for m in range(i+1,n-i):
                mat[m][-1-i] = val
                val +=1
            for m in range(n-2-i,i-1,-1):
                mat[-1-i][m] = val
                val +=1
            for m in range(n-2-i,i,-1):
                mat[m][i] = val
                val +=1
        if val == n**2:
            mat[n//2][n//2] = val
        return mat
            
            