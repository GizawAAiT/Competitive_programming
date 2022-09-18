class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R,C =len(grid),len(grid[0])
        q = []
        space = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] ==2:
                    q.append((i,j))
                elif grid[i][j]==0:
                    space+=1
        rot = len(q)
        step = 0
        while q and rot < R*C - space: 
            l = len(q)
            for _ in range(l):
                (i,j) = q.pop(0) 
                for a,b in [(i+1,j),(i,j-1),(i,j+1),(i-1,j)]:
                    if a>=0 and a<R and b>=0 and b<C and grid[a][b]==1:
                        grid[a][b]=2
                        q.append((a,b))
            rot += len(q)
            # print(q,rot)
            step+=1
        return step if rot == R*C - space else -1
            