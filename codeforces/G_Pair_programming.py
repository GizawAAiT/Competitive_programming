n, k = (int(_) for _ in input().split())
arr = [int(_) for _ in input().split()]
arr.sort()
left = time = 0
x = len(arr)
while left < x:
    half = (x-left)//2
    left += half
    time += half * arr[left-1]
    k -= half
    if k <= 0:
        time += k * arr[left-1]
        print(time)
        break


