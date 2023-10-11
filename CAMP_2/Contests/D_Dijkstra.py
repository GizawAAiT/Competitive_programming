from collections import defaultdict
import heapq

n, m = (int(_) for _ in input().split())


children = defaultdict(list)
for _ in range(m):
    u, v, w = (int(_) for _ in input().split())
    children[u].append((v, w))
    children[v].append((u, w))

que = [(0, 1, 0)]
parent = defaultdict()
# parent[1] = 0
visited = set()
path = []
while que:
    cost, node, par = heapq.heappop(que)

    if node in visited:
        continue

    visited.add(node)
    
    parent[node] = par

    if node == n:
        while node != 0:
            path.append(node)
            node = parent[node] 
        break

    for child, weight in children[node]:
        if child not in visited:
            heapq.heappush(que, (cost+weight, child, node))

# print(parent)       
if path:
    print(*reversed(path))

else:
    print(-1)

        
