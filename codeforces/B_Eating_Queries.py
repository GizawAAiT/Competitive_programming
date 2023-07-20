t = int(input())

def binary(arr, n, target):
    left, right = 0, n
    while right > left + 1:
        mid = (right+left)//2
        if arr[mid] < target:
            left = mid
        else:
            right = mid
    # print((left, right, arr, target))
    return right if right < n and arr[right] >= target else -1

for _ in range(t):
    n, q = (int(_) for _ in input().split())

    arr = [int(_) for _ in input().split()]

    arr.sort(reverse= True)

    for i in range(1, n):
        arr[i] += arr[i-1]
    arr.insert(0, 0)
    for _ in range(q):
        target =  int(input())
        ans = binary(arr, n + 1, target)
        print(ans)
    

    
