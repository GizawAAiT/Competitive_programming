from collections import defaultdict
from sys import stdin, stdout
 
 
def inp():
    return int(stdin.readline())
 
 
def inlt():
    return list(map(int, stdin.readline().strip().split()))
 
 
def insr():
    s = stdin.readline().strip()
    return list(s[:len(s)])
 
 
def invr():
    return map(int, stdin.readline().strip().split())
 
def main():
    n, m = inlt()
    grid = [[0 for i in range(101)] for _ in range(101)]
 
    for _ in range(n):
        x, y = inlt()
        grid[x][y] += 1
 
    
    for _ in range(m):
        sx, sy, ex, ey =  inlt()
        ans = 0
        for i in range(sx, ex+1):
            for j in range(sy, ey+1):
                ans += grid[i][j]
        print(ans)
 
main()