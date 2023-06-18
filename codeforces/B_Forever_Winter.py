from collections import defaultdict
t = int(input())

for _ in range(t):
    n, m = (int(_) for _ in input().split())
    graph = defaultdict(list)

    for _ in range(m):
        u, v = (int(_) for _ in input().split())
        graph[u].append(v)
        graph[v].append(u)


    leaf = None
    for k in graph:
        if len(graph[k]) == 1:
            leaf = k
            break

    parent = graph[leaf][0]
    grandpa = None
    for grand in graph[parent]:
        if len(graph[grand]) != 1:
            grandpa = grand
            break
    print(len(graph[grandpa]), len(graph[parent])-1)


