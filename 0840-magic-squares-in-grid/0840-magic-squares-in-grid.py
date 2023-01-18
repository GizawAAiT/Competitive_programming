class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        
        def isMagic(i,j):
            test_set = set()
            #3 rows.
            for r in range(i-1, i+2):
                test_set.add(sum([grid[r][_] for _ in range(j-1,j+2)]))
            #3 cols.
            for c in range(j-1, j+2):
                test_set.add(sum([grid[_][c] for _ in range(i-1,i+2)]))
            #2 duaginals
            test_set.add(sum([grid[i-1][j-1], grid[i][j], grid[i+1][j+1]]))
            test_set.add(sum([grid[i-1][j+1], grid[i][j], grid[i+1][j-1]]))
            print((i,j),test_set)
            if len(test_set)>1: return False
            
            s = set()
            for a in range(i-1,i+2):
                for b in range(j-1,j+2):
                    s.add(grid[a][b])
            # for n in grid[i-1:i+2][j-1:j+2]:s.add(n) 
            print(s)
            if len(s)<9: return False
             
            for x in range(1,10): 
                if x not in s:
                    return False
            return True
        
        magic_count = 0
        for i in range(1,len(grid)-1):
            for j in range(1,len(grid[0])-1):
                if grid[i][j] ==5 and isMagic(i,j):
                    magic_count +=1
        return magic_count
            