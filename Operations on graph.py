from collections import defaultdict
vertices = int(input())
n = int(input())

neighbours = defaultdict(list)
for _ in range(n):
    I = input().split()
    if I[0] == '1':
        neighbours[I[1]].append(I[2])
        neighbours[I[2]].append(I[1])
    elif I[1] in neighbours:
        print(*neighbours[I[1]]) 
    else:
        print()