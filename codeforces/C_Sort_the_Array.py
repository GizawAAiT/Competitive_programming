n = int(input())
nums = [int(_) for _ in input().split()]

i = 1
while i<n and nums[i]>nums[i-1]: i+=1
if i ==n:
    print('yes')
    print(nums[0], nums[0])

else:
    j = i
    while j<n and nums[j]<nums[j-1]: j+=1
    if j == n:
        print('yes')
        print(nums[-1], nums[0])
    else:
        j-=1
        l, r = nums[i], nums[j]
        while i<j:
            nums[i],nums[j] = nums[j], nums[i]
            i+=1
            j-=1
        if nums == sorted(nums):
            print('yes')
            print(l,r)
        else:
            print('no')


