from collections import deque
directions = [(0, 1), (1, 0), (1, 1), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1)]
def inbound(row, col):
    return 1 <= row <= 10**9 and 1 <= col <= 10**9 

x0,y0, x1,y1 = (int(_) for _ in input().split())
n = int(input())
allowed = set()
for _ in range(n):
    r, a, b = (int(_) for _ in input().split())
    for _ in range(a, b + 1):
        allowed.add((r, _))

Q = deque([(x0, y0, 0)])
visited = set([(x0, y0)])

def bfs():
    
    minDepth = -1
    
    while Q:
        row, col, depth = Q.popleft() 
        
        for dx, dy in directions:
            newRow, newCol = row + dx, col + dy
            if inbound(newRow, newCol) and (newRow, newCol) in allowed and (newRow, newCol) not in visited:
                if (newRow, newCol) == (x1, y1):
                    # print(newRow, newCol, "===", (x1, y1), depth + 1)
                    minDepth = depth + 1
                    return minDepth
                

                Q.append((newRow, newCol, depth + 1))
                visited.add((newRow, newCol)) 
    return -1

print(bfs())