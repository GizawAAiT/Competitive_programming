t = int(input())

for _ in range(t):
    n = int(input())
    nums = [int(_) for _ in input().split()]
    
    maximum = nums[0]
    result = []
    for i in range(1, n):
        if nums[i] < 0 and nums[i-1] < 0 or nums[i] > 0 and nums[i-1] > 0:
            maximum = max(maximum, nums[i])
        
        else:
            result.append(maximum)
            maximum = nums[i]

    result.append(maximum)
    print(sum(result))


