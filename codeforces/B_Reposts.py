from collections import defaultdict
from collections import deque
n = int(input())

reposter = defaultdict(list)
for _ in range(n):
    A, _, B = input().split(' ')
    reposter[B.lower()].append(A.lower()) 
# print(reposter)
def bfs(root,length):
    visited = set([root])
    Q = deque([root])
    # length = 0
    while Q:
        length += 1
        size = len(Q)

        for _ in range(size):
            node = Q.popleft() 

            for child in reposter[node]:
                Q.append(child) 
                visited.add(child)
                    

    # print(visited, '==', 'visited')
    return length
print(bfs("polycarp", 0)) 



