from math import *
def solve(n, d):
    x = sqrt(d)
    if floor(x) + ceil(d/(floor(x) + 1)) <= n:
        return "YES"
    if floor(x) - 1 + ceil(d/(floor(x))) <= n:
        return "YES"
    # for x in range(d//2 + 1):
    #     if x + ceil(d/(x+1)) <= n: return True
    return "NO"
    
T = int(input())
for _ in range(T):
    n, d = (int(_) for _ in input().split())
    print(solve(n, d))
