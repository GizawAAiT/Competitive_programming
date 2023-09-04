def solve(arr, n):
    count = 0
    left = 0
    for right in range(n):
        while arr[left ] != arr[right]:
            left += 1

        if (right == n-1 or arr[right+1]>arr[right]) and (left == 0 or arr[left-1] > arr[left]):
            count += 1
    
    return "YES" if count == 1 else "NO"

t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(_) for _ in input().split()]
    print(solve(arr, n))
    