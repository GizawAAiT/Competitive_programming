t = int(input())
for _ in range(t):
    s = input()
    res = set()
    i = 0
    while i<len(s)-1:
        if s[i] == s[i+1]:
            j = i+1
            while j<len(s) and s[j] == s[i]: j+=1
            if (j-i)%2: res.add(s[i])
            i = j
        else:
            res.add(s[i])
            i+=1
    if i < len(s):
        res.add(s[i])
    print(''.join(sorted(list(res))))


