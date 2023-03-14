n = int(input())
nums = [int(_) for _ in input().split()]
nums.sort()
if nums[-1]!=nums[0]:
    for n in nums:
        print(n, end=' ')
else: 
    print(-1)