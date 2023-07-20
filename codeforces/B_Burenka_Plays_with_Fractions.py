t = int(input())
for _ in range(t):
    a, b, c, d = (int(_) for _ in input().split())
    if a/b == c/d:
        print(0)

    elif a==0 or c == 0 or (0 in [(a*d)%c, (a*d) % b, (b*c)%a, (b*c)%d]):
        print(1)
    else:
        print(2)
    