n = int(input())
a = [int(_) for _ in input().split()]
b = [int(_) for _ in input().split()]

a.sort()
b.sort()
score = 0
p1 = p2 = n-1
while p1 > -1 and p2 > -1:
    while p1 >= 0 and b[p2] < a[p1] :
        p1 -= 1
    if p1 >= 0 and b[p2] >= a[p1]:
        score += 1
    p2 -= 1
    p1 -= 1

print((n-score + 1)//2)