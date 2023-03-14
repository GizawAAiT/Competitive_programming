n, m = (int(_) for _ in input().split())
pref = [0 for i in range(n+1)]
for _ in range(m):
    i,j = [int(_) for _ in input().split()]
    pref[i] += 1
    pref[j+1] -= 1
for i in range(1,len(pref)):
    pref[i] += pref[i-1]
ans = 'NO'
for i in range(n):
    if pref[i] == 0:
        ans = 'YES'
        break
print(ans)