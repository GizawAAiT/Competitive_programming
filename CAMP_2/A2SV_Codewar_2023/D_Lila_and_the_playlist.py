n, p = (int(_) for _ in input().split())
arr = [int(_) for _ in input().split()]

total = sum(arr)

loop = p//total
p = p%total

left = 0
answer = n
indx = 0
for right in range(2*p):
    p-= arr[right%n]
    while p + arr[left%n] <= 0:
        p += arr[left%n] 
        left += 1
    if p<= 0 and answer >  right-left+1:
        answer = min(answer, right-left+1)
        indx = left%n
    
c = answer + loop*n
print(*[indx+1, c])