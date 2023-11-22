class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def helper(r,c):
            vals = set()
            for i in range(r[0],r[1]):
                for j in range(c[0],c[1]):
                    if board[i][j].isdigit() and board[i][j] in vals:
                        return False
                    vals.add(board[i][j])
            return True
        for i in range(9):
            if not helper((i,i+1),(0,9)): return False
        for j in range(9):
            if not helper((0,9),(j,j+1)): return False
        for i in range(0,7,3):
            for j in range(0,7,3):
                if not helper((i,i+3),(j,j+3)): return False
        return True
    """
[[".",".",".",".",".",".","5",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],["9","3",".",".","2",".","4",".","."],[".",".","7",".",".",".","3",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".","3","4",".",".",".","."],[".",".",".",".",".","3",".",".","."],[".",".",".",".",".","5","2",".","."]]"""