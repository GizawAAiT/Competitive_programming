from collections import defaultdict


t = int(input())
for _ in range(t):
    n, m = [int(i) for i in input().split()]
    arr = []
    for _ in range(n):
        cur = [int(i) for i in input().split()]
        arr.append(cur)
    
    dif = defaultdict(int)
    dsum = defaultdict(int)
    for i in range(n):
        for j in range(m):
            dif[i-j] += arr[i][j]
            dsum[i+j] += arr[i][j]
    
    max_sum = 0
    for i in range(n):
        for j in range(m):
            max_sum = max(max_sum, dif[i-j] +  dsum[i+j]-arr[i][j])
    print(max_sum)
