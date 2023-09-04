class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        
        if m*n != r*c: return mat
        
        reshaped = [[0 for _ in range(c)] for _ in range(r)]
        
        for x in range(m*n):
            reshaped[x//c][x%c] = mat[x//n][x%n]
        return reshaped