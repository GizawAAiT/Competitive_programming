t = int(input())
for _ in range(t):
    n = int(input())
  
    ans = [n, n-1]
    
    for i in range(1, n-1):
        ans.append(i)
    if n == 3:
        print(-1)
    else:
        print(*ans )