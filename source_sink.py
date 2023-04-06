from collections import defaultdict
n = int(input())

row_sum, col_sum  = defaultdict(int), defaultdict(int)

for i in range(n):
    for j, val in enumerate((input().split())):
        row_sum[i+1] += int(val)
        col_sum[j+1] += int(val)


sources, sinks = [], []
for value, count in row_sum.items():
    if count == 0:
        sinks.append(value)

for value, count in col_sum.items():
    if count == 0:
        sources.append(value)

sources.sort()
sinks.sort()
print(len(sources), *sources)
print(len(sinks), *sinks)