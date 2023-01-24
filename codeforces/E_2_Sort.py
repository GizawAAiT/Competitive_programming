t = int(input())
for _ in range(t):
    n, k = (int(x) for x in input().split())
    arr = [int(x) for x in input().split()]
    res, w = 0, 1

    for i in range(1,n):
        if arr[i]*(2**w) > arr[i-1]*(2**(w-1)):
            w += int(w<=k)
        else: w = 1
        res += int(w==k+1)
    print(res)





