s = input()
t = input()
i, j = len(s)-1, len(t)-1
while i>=0 and j>=0 and s[i] == t[j]:
    i-= 1
    j-= 1

print(i+j+2)
    