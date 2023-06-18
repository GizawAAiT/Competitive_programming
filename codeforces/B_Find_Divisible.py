T = int(input())

def f(l, r):
    for i in range(l, r + 1):
        if 2 * i <= r:
            return (i, 2 * i)


for _ in range(T):
    l, r = (int(_) for _ in input().split())

    print(*f(l, r))


