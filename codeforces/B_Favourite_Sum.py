t = int(input())
for _ in range(t):
    n, x = (int(_) for _ in input().split())
    favorite = [int(_) for _ in input().split()]
    for _ in range(n):
        if favorite[_] > x:
            favorite[_] = 0
    print(((1+x)*x)//2 - 2*sum(favorite))


