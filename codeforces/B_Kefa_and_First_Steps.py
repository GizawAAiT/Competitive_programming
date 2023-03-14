n = int(input())
a = [int(_) for _ in input().split()]

length = 1
mx = 1
for i in range(1,n):
    if a[i]>=a[i-1]:
        length+=1
    else: length=1
    mx= max(mx, length)
print(mx)
