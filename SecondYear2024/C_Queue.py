n = int(input())
times = [int(_) for _ in input().split()]

satisfied = 0
times.sort()
idx = 0
for t in times:
    if idx <= t:
        satisfied += 1
        idx += t
print(satisfied)