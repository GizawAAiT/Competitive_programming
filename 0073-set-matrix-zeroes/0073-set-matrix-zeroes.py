class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_in_row, zero_in_col= set(), set()
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] ==0:
                    zero_in_row.add(i)
                    zero_in_col.add(j)
        
        for r in range(len(matrix)):
            if r in zero_in_row:
                for c in range(len(matrix[0])):
                    matrix[r][c] =0
        for c in range(len(matrix[0])):
            if c in zero_in_col:
                for r in range(len(matrix)):
                    matrix[r][c] =0
        