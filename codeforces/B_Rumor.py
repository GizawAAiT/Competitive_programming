from collections import defaultdict, deque
n, m = (int(_) for _ in input().split())
c = [int(_) for _ in input().split()]

nei = defaultdict(list)
for _ in range(m):
    a, b =[int(_) for _ in input().split()]
    nei[a-1].append(b-1)
    nei[b-1].append(a-1)

visited = set()
def bfs(i):
    cost = float('inf')
    que = deque([i])
    
    while que:
        node = que.popleft()
        visited.add(node)
        cost = min(cost, c[node])
        for neig in nei[node]:
            if neig not in visited:
                que.append(neig)
    return cost 



total_ = 0

for i in range( n):
    if i not in visited:
        total_ += bfs(i)
print(total_)

