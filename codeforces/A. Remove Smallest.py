t = int(input())
for _ in range(t):
    n = int(input())
    nums = [int(_) for _ in input().split()]
    nums.sort()
    while len(nums)>1:
        if nums[-1] == nums[-2] or nums[-1] == nums[-2]+1:
            nums.pop()
        else: 
            break
    if len(nums) ==1: print('YES')
    else: print('NO')