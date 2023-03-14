t = int(input())
for _ in range(t):
    n = int(input())
    nums = [int(_ ) for _ in input().split()]
    i , j= 0, n-1
    while i<j:
        print(nums[i],nums[j],end=' ')
        i+=1
        j-=1
    if i==j:
        print(nums[j])
    else: print()