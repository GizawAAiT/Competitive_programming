h = 'hello'
s = input()
i, j = 0, 0
while i<len(h) and j < len(s):
    if h[i] == s[j]:
        i += 1
    j += 1
if i == len(h):
    print("YES")
else:
    print('NO')