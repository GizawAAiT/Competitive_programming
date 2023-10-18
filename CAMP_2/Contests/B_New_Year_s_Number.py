t = int(input())
for _ in range(t):
    n = int(input())
    qou, rem = n//2020, n%2020
    if qou >= rem:
        print("YES")
    else:
        print("NO")