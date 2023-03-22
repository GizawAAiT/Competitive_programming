from math import ceil
N, D = (int(_) for _ in input().split())
players = [int(_) for _ in input().split()]
players.sort(reverse=True)
i =  0

while N > 0:
    n = ceil(D/players[i])
    N -= n if players[i]*n > D else n+1
    i += 1
if N == 0:
    print(i)
else:
    print(i-1)

    