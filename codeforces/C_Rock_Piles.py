T = int(input())
for _ in range(T):
    N, M = (int(_) for _ in input().split())
    if N%2 == 0 and M%2 == 0:
        print("abdullah")
    else:
        print("hasan")
