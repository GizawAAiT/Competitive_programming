t = int(input())
for _ in range(t):
    # print('.........')
    n = int(input())
    grid = []
    for _ in range(n):
        grid.append([int(_) for _ in input()])
    res = 0
    for i in range(n//2):
        # l = []
        for j in range(i,n-i-1):
            l = [grid[i][j], grid[j][n-1-i], grid[n-1-i][n-1-j], grid[n-1-j][i]]
            # print(l)
            if sum(l) in [1,3]: res += 1
            elif sum(l) == 2: res += 2
    print(res)
    # print('..........')
    