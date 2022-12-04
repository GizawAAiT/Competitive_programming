class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        tot =0
        for i in range(len(mat)):
            tot+=(mat[i][i]+mat[i][-1-i])
        return tot-mat[len(mat)//2][len(mat)//2] if len(mat)%2 else tot