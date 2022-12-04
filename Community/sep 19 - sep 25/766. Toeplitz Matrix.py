class Solution:
    def isToeplitzMatrix(self, mat: List[List[int]]) -> bool:
        R,C=len(mat),len(mat[0])
        if R==1 or C==1:
            return True
        for i in range(1,R):
            for j in range(1,C):
                if mat[i][j]!=mat[i-1][j-1]:
                    return False
        return True