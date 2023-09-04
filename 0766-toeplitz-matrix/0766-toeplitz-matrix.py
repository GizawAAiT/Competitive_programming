class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        freq = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i-j in freq and matrix[i][j]!=freq[i-j]: return False
                freq[i-j] = matrix[i][j]
        return True