n, k = (int(_) for _ in input().split())

nums = [int(_) for _ in input().split()]
nums.sort()
nums.append(float('inf'))
if k == 0:
    print(1) if nums[0]!=1 else print(-1)
elif nums[k] != nums[k-1] and nums[k-1] <=10**9:
    print(nums[k-1])
else:
    print(-1)