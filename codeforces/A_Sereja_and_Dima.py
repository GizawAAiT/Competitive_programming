n = int(input())
nums = [int(_) for _ in input().split()]

score = [0,0]
i,j = 0, n-1
while i<=j:
    if nums[i]>nums[j]:
        score[0]+= nums[i]
        i+=1
    else:
        score[0]+= nums[j]
        j-=1
    score[0], score[1] = score[1], score[0]
if n%2:
    score[0], score[1] = score[1], score[0]
print(*score)

