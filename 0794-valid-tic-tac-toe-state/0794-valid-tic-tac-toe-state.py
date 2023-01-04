class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        
        x = o = 0
        for b in board:
            for ch in b:
                x += int(ch=='X')
                o += int(ch=='O')
        
        def similar(arr):
            t = arr[0]
            for a in arr: 
                if a!=t: return False
            return t
        
        array = [list(board[0]),list(board[1]),list(board[2]),[w[0] for w in board], [w[1] for w in board],[w[2] for w in board],[board[0][0], board[1][1], board[2][2]],[board[0][2], board[1][1], board[2][0]]]
        
        if x not in [o, o+1]: return False #unproportianal 0 and X 
        for arr in array:
            if similar(arr) == 'X' and x==o or similar(arr) == 'O' and x==o+1: return False
        return True
        