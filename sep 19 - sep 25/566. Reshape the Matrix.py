class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        R,C=len(mat),len(mat[0])
        if R*C != r*c:
            return mat
        new = [[None]*c for _ in range(r)]      
                
        i,j,a,b = 0,0 ,0,0     
        
        while i<R and j<C: 
            new[a][b]=mat[i][j]
            if j+1==C:
                i,j=i+1,0
            else:
                j+=1
            if b+1==c:
                a,b=a+1,0
            else:
                b+=1
        return new
            
        