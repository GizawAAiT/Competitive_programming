t = int(input())
for _ in range(t):
    n, m = (int(_) for _ in input().split())
    a = [int(_) for _ in input().split()]
    a.sort()
    a.reverse()
    outlets = 2
    index = 0
    while index<m and outlets<n:
        outlets += a[index]-1 
        index += 1
    if outlets<n:
        print(-1)
    else:
        print(index)