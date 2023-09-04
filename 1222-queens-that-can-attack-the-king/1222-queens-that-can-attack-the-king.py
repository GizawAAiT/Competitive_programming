class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        
        queens = set([tuple(queens[i]) for i in range(len(queens))]) 
        direct_attackers = []
        
        #helper function to move in all 8 directions from (i,j):
        def move(i,j,di,dj):
            while i<8 and j<8 and i>=0 and j>=0:
                if (i,j)  in queens:
                    direct_attackers.append([i,j])
                    return
                i+= di
                j+= dj
        
        i, j = king[0], king[1]
        print(i,j)
        move(i,j+1,0,1)
        move(i+1,j+1,1,1)
        move(i+1,j,1,0)
        move(i+1,j-1,1,-1)
        move(i,j-1,0,-1)
        move(i-1,j-1,-1,-1)
        move(i-1,j,-1,0)
        move(i-1,j+1,-1,1)
        
        return direct_attackers
        
        
                
        
        
        
        