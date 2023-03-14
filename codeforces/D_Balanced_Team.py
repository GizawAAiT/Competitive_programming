n = int(input())
a = [int(_) for _ in input().split()]

a.sort()

i , j = 0, 0
res = 1
while j<n:
    if a[j]-a[i]<=5:
        j+=1
        
    else:
        i +=1
    res = max(res, j-i)
res = max(res, j-i)
print(res)