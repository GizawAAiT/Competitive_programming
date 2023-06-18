t = int(input())
for _ in range(t):
    n, time = (int(_) for  _ in input().split())
    a = [int(_) for  _ in input().split()]
    b = [int(_) for  _ in input().split()]
    
    answer = -float('inf')
    indx = 0
    for i in range(n):
        if a[i] + i <= time and answer <  b[i]:
            indx = i
            answer = b[indx]
    
    print(indx + 1 if answer != -float('inf') else -1)
    