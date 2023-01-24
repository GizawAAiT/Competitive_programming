t = int(input())
for _ in range(t):
    nums = [int(_) for _ in input().split()]
    nums.sort()
    print(nums[1])