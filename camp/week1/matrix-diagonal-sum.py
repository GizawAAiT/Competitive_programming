class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
             
            s, i = 0, 0
            while i < len(mat):
                s += mat[i][i] + mat[i][len(mat)-1-i]
                i+=1
            if len(mat)%2==1:
                s -= mat[len(mat)//2][len(mat)//2]
            return s