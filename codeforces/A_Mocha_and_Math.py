t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(_) for _ in input().split()]
    
    for _ in range(5):
        minimum = min(arr)
        for _ in range(n):
            arr[_] &= minimum
    # minimum = min(arr)
    # for _ in range(n):
    #     arr[_] &= minimum
    print(min(arr))
