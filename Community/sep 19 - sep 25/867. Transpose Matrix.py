class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        R,C=len(matrix),len(matrix[0])
        new = [[i] for i in matrix[0]]
        for i in range(1,R):
            for j in range(C):
                new[j].append(matrix[i][j]) 
        return new
