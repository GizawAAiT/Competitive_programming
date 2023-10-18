from collections import defaultdict
topologies = ["bus topology", "star topology", "ring topology", "unknown topology"]

n, m = [int(_) for _ in input().split()]
indegree = defaultdict(int)
for _ in range(m):
    u, v = (int(_) for _ in input().split())
    indegree[u] += 1
    indegree[v] += 1
    # if indegree[u] >2 or indegree[v] >2:
    #     answer = topologies[-2]
    #     break

degree = sorted(indegree.values())
if degree[-1] > 2 and degree[-2] == 1:
    print(topologies[1]) 
elif degree[0] == degree[-1] == 2:
    print(topologies[2])
elif degree[0] == degree[1] == 1 and degree[2] == degree[-1] == 2:
    print(topologies[0])
else:
    print(topologies[-1])

