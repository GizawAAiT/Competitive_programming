class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R,C=len(board),len(board[0])
        path = set()
        def scn(i,j,k):
            global vis
            if k==len(word): return True 
            if (i<0 or j<0 or i>=R or j>=C or word[k]!=board[i][j]or(i,j) in path):
                return   
            path.add((i,j)) 
            res=(scn(i+1,j,k+1)or scn(i,j+1,k+1)or scn(i-1,j,k+1)or scn(i,j-1,k+1))
            path.remove((i,j))
            return res
        for i in range(R):
            for j in range(C):
                if board[i][j]==word[0] and scn(i,j,0): return True 
        return False
            
        