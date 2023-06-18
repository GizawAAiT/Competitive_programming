from collections import defaultdict, deque

v, e = (int(_) for _ in input().split())

edges = []
undirected = defaultdict(list)

for _ in range(e):
    u, v = input().split()
    edges.append((u, v))
    undirected[u].append(v)
    undirected[v].append(u)
    directed = defaultdict(list)

    root = edges[0][0]
    que = deque([root])
    reverse = False
    new_edges = []
    while que:
        size = len(que)
        for _ in range(size):
            u = que.popleft()
            for v in undirected[u]:
                if reverse:
                    directed[u].append(v)
                    new_edges.append((u, v))

                else:
                    directed[v].append(u)
                    new_edges.append((v, u))
        reverse = not reverse

    result 
    
            

