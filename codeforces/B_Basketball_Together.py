from math import *
N, D = (int(_) for _ in input().split())

powers = [int(_) for _ in input().split()]

powers.sort(reverse= True)
res = indx = players = 0
while players < N:
    cur_players = floor(D/powers[indx]) + 1
    if cur_players + players <= N :
        res += 1
    players += cur_players
    
    indx += 1

print(res)

