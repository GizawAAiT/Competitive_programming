n,k , q = (int(_ ) for _ in input().split())

pref = [0 for _ in range(200002)]
for i in range(n):
    l, r = (int(_) for _ in input().split())
    pref[l] +=1 
    pref[r+1] -=1
for i in range(1,200002):
    pref[i] += pref[i-1]
pref2 = [1 if pref[i] >=k else 0 for i in range(200002)]
for i in range(1,200002):
    pref2[i] += pref2[i-1]
for i in range(q):
    l, r = (int(_) for _ in input().split())
    count = pref2[r] - pref2[l-1]
    
    
    print(count)
    



