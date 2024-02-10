def prefix(s):
    pre = [0]
    for i in range(1, len(s)):
        pre.append(int(s[i-1]==s[i]))
    
    for i in range(1, len(pre)):
        pre[i] += pre[i-1]
    
    return pre

s = input()
pre = prefix(s)
for _ in range(int(input())):
    i, j = (int(_) for _ in input().split())
    print(pre[j-1]-pre[i-1])

