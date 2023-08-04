T = int(input())
from collections import Counter
for _ in range(T):
    a, b = (input().split())
    count = Counter(b)
    i = 0
    while i < len(a):
        if count[a[i]] < 1:
            break
        count[a[i]] -= 1
        i += 1
    print(i)


