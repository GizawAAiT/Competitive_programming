class Solution:
    def totalNQueens(self, n: int) -> int:
        
        def check(points, row, col):
            
            for prow, pcol in points:
                if prow - pcol == row - col:
                    return False
                
                if prow + pcol == row + col:
                    return False
                
                if prow == row or pcol  == col:
                    return False
                
            return True
        
        points = []
        
        def backtrack(row):
            if row == n: 
                return 1
            
            count = 0
            for col in range(n):
                if check(points, row, col):
                    points.append((row,col))
                    count += backtrack(row+1) 
                    points.pop()
                    
            return count
                    
        
        return backtrack(0)
            