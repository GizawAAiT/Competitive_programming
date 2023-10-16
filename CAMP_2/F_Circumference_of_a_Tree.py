from collections import defaultdict
n = int(input())
graph = defaultdict(list)
indegree = defaultdict(int)

for _ in range(n-1):
    u, v = [int(_) for _ in input().split()]
    indegree[u] += 1
    indegree[v] +=1
    graph[u].append(v)
    graph[v].append(u)
que = []
for node in graph:
    if indegree[node] <= 1:
        que.append(node)
diameter = 0     
while que:
    
    size = len(que)
    for _ in range(size):
        node = que.pop()
        for child in graph[node]:
            indegree[child] -= 1
            if indegree[child] == 1:
                que.append(child)
    if que:
        diameter += 2
    else:
        diameter += 1

if n == 1:
    print(0)
elif n == 2:
    print(3)
else:
    print(3*(diameter))
    # print(radius)
