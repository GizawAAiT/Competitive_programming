n = int(input())
nums = [int(_) for _ in input().split()]
res = 0
count_neg = 0
count_zeros = 0
for n in nums:
    res += (min(abs(n-1), abs(n+1)))
    count_neg += int(n<0)
    count_zeros += int(n==0)

if count_neg%2==0 or count_zeros>=1:
    print(res)
else:
    print(res+2)