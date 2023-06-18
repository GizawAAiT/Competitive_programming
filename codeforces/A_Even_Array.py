t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(_) for _ in input().split()]

    x = [0, 0]
    for i in range(n):
        if i%2 != arr[i] %2:
            x[i%2] += 1
    if x[0] == x[1]:
        print(x[0])
    else:
        print(-1)