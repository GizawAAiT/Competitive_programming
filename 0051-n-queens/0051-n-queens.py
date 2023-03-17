class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def check(points, row, col):
            
            for prow, pcol in points:
                # check row & col:
                if prow == row or pcol == col:
                    return False
            
                # check diagonal_1:
                if prow + pcol == row + col:
                    return False
                
                # check diagonal_2:
                if prow - pcol == row - col:
                    return False
                
            return True
        
        points = []
        answer = []
        
        def solution(row):
            if row == n:
                cur = [['.' for col in range(n)]  for row in range(n)]
                for row, col in points:
                    cur[row][col] = 'Q'
                for row in range(n):
                    cur[row] = ''.join(cur[row])
                answer.append(cur)
                
                return 
            
            for col in range(n):
                if check(points, row, col):
                    points.append((row, col))
                    solution(row + 1)
                    points.pop()
            return 
        
        solution(0)
        return answer