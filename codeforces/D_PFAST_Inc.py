from collections import defaultdict, deque
n, m = (int(_) for _ in input().split())
names = []
graph = defaultdict(list)
for _ in range(n):
    names.append(input())

for _ in range(m):
    u, v = input().split()
    graph[u].append(v)
    graph[v].append(u)

result = []
visited = set()
for name in names:
    if name in visited:
        continue
    
    even = [name]
    odd = []
    level = 0
    que = deque([name])
    visited.add(name)
    while que:
        level = 1 -level
        size = len(que)
        
        for _ in range(size):
            node = que.popleft()
            
            for child in graph[node]:
                
                if child not in visited:
                    if level == 0:
                        even.append(child)
                    else:
                        odd.append(child)
                    que.append(child)
                    visited.add(child)

    if len(even) >= len(odd):
        result.extend(even)
    else:
        result.extend(odd)
print(len(result))
result.sort()
for _ in range(len(result)):
    print(result[_])
    







