n = int(input())
nums = [int(_) for _ in input().split()]
count = 0
swaps = []
for i in range(n-1):
    j = i
    for _ in range(j, n):
        if nums[_]<nums[j]:
            j=_
    if j!=i:
        nums[i],nums[j]= nums[j], nums[i]
        swaps.append((i,j))
        count += 1 
if count == 0:
    print(0)
else:
    print(len(swaps))
    for s in swaps:
        print(s[0],s[1])
