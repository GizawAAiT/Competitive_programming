t = int(input())
for i in range(t):
    n = int(input())
    nums = [int(_) for _ in input().split()]
    left = 0
    cur = 0
    count = 0
    for right in range(n-1):
        cur += nums[right]
        while left < right and cur > 0 and nums[right]==0:
            nums[left] -= 1
            nums[right] += 1
            if nums[left] == 0:
                left+=1
            count += 1
    print(count + cur)
        

