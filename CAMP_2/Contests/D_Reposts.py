n = int(input())
from collections import deque, defaultdict
graph = defaultdict(list)

for _ in range(n):
    end, _, start = input().split()
    graph[start.lower()].append(end.lower())

que = deque(['polycarp'])
depth = 0
while que:
    depth += 1
    length = len(que)
    for _ in range(length):
        node = que.popleft()
        for child in graph[node]:
            que.append(child)

print(depth)



