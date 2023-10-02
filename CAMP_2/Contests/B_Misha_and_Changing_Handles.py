from collections import defaultdict
q = int(input())

parent = defaultdict()

last_halndles = set()
for _ in range(q):
    old, new = input().split()
    if old in last_halndles:
        last_halndles.remove(old)
    last_halndles.add(new)
    parent[new] = old

ans = []
for child in last_halndles:
    par = parent[child]
    temp = child
    while par in parent.keys():
        child, par = par, parent[par]
    ans.append((par, temp))
print(len(ans))
for tup in ans:
    print(*tup)

