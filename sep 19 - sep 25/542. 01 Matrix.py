class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        D = [[float("inf")]*len(mat[0]) for _ in range(len(mat)) ]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==0:
                    D[i][j]=0
                if i>0:
                    D[i][j]=min(D[i][j],1+D[i-1][j])
                if j>0:
                    D[i][j]=min(D[i][j],1+D[i][j-1])       
        
        for i in range(1,len(mat)+1):
            for j in range(1,len(mat[0])+1):                
                if i>1:
                    D[-i][-j]=min(D[-i][-j],1+D[-i+1][-j])
                if j>1:
                    D[-i][-j]=min(D[-i][-j],1+D[-i][-j+1])
        
        return D