from collections import deque
t = int(input())
directions = [(0, 1), (1, 0), (1, 1), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1)]
def inbound(row, col):
    return 1 <= row <=10**9 and 1 <= col <=10**9 

def bfs(root, bit):
    if bit[root[0]][root[1]] == '1': return False
    visited = set([root])
    Q = deque([root])
    # length = 0
    while Q:
        row, col = Q.popleft()
        for dx, dy in directions:
            newRow, newCol = row + dx, col + dy
            if inbound(newRow, newCol, n) and (newRow, newCol) not in visited :
                if bit[newRow][newCol] == '0':
                    if (newRow, newCol) == (1, n-1):
                        return True
                    Q.append((newRow, newCol))
                    visited.add((newRow, newCol))
    return False

x0,y0, x1,y1 = (int(_) for _ in input().split())
n = int(input())
allowed = set()
for _ in range(n):
    r, a, b = (int(_) for _ in input().split())
    for _ in range(a, b + 1):
        allowed.add((r, _))


Q = deque([(x0, y0, 0)])
minDepth = -1
while Q:
    row, col, depth = Q.popleft() 
    
    for dx, dy in directions:
        newRow, newCol = row + dx, col + dy
        if inbound(newRow, newCol) and (newRow, newCol) in allowed :
            if bit[newRow][newCol] == '0':
                if (newRow, newCol) == (x1, y1):
                    minDepth = depth
                    break
                Q.append((newRow, newCol, depth + 1))
print(minDepth)