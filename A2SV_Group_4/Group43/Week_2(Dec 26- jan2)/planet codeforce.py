from collections import Counter

t = int(input())
for _ in range(t):
    n, c = ([int(i) for i in input().split()])
    planets = [int(i) for i in input().split()]
    planets = Counter(planets)
    res = 0
    for p in planets:
        res += min(c, planets[p])
    print(res)