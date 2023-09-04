n = int(input())

for i in range(1, n+1):
    neighbours = []
    for i, v in enumerate(input().split()):
        if v != '0':
            neighbours.append(i+1)
    
    if len(neighbours) != 0:
        print(len(neighbours), * neighbours)
