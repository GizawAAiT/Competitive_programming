class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary(x, y):
            if x >= len(matrix[0]) or y < 0:
                return False
            
            if matrix[y][x] == target: return True
            return binary(x+1, y) if target > matrix[y][x] else binary(x, y-1)
        
        return binary(0, len(matrix)-1)