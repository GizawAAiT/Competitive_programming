n, x, y = (int(_) for _ in input().split())
from math import *
def solve(n, x, y):
    n -= 1
    x, y = min(x,y), max(x, y)
    copies1, copies2 = ceil((x/(x+y))*n), ceil((y/(x+y))*n)
    return min(copies1 * y, copies2 *x) + x
print(solve(n, x, y)) 