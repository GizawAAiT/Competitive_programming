n,m,s, wa, wb = (int(_) for _ in input().split())
a = [int(_) for _ in input().split()]
b = [int(_) for _ in input().split()]
a.sort(reverse=True)
b.sort(reverse=True)

# cummulate
for i in range(1, len(a)):
    a[i] += a[i-1]
for i in range(1, len(b)):
    b[i] += b[i-1]

i = len(a)-1
# maxVal = 0
value = a[i]
while wa*i > s:
    i -= 1
    value = a[i]
maxVal = a[i]
answer = i + 1
j = 0
while i>=0:
    i-= 1
    value = a[i]
    while j < len(b) and 

    






