t = int(input())
for _ in range(t):
    n = int(input())

    nums = [int(_) for _ in input().split()]
    # nums.sort()
    
    # j = n-1
    # while j > 0 and nums[j]&1==0:
    #     j -= 1
    # if nums[j] & 1 and nums[j] != 1:
    #     nums[j], nums[-1] = nums[-1], nums[j]
    k = 0
    for i in range(n):
        while nums[i]!=0 and nums[i] & 1 == 0:
            nums[i] >>= 1
            k += 1
    nums.sort()
    nums[-1] <<= k
    print(sum(nums))