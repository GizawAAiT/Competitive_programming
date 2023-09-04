class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix[0]), len(matrix)
        i = -1
        j = len(matrix)*len(matrix[0])
        
        while i<j-1:
            mid = (i+j) //2
            
            r, c = mid//m, mid%m
            if matrix[r][c] == target: return True
            if matrix[r][c] > target: 
                j = mid
            else: i = mid
        # return False
            
            
        