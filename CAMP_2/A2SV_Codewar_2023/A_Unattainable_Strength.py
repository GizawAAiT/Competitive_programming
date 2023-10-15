n = int(input())
x = [int(_) for _ in input().split()]
x.sort()
def solve(n):
    cum = 0
    xi = 0
    num = 1
    while True:
        while xi < n and x[xi] <= num:
            cum += x[xi]
            xi += 1
        if cum < num:
            return num
        num = cum+1
        
print(solve(n))
