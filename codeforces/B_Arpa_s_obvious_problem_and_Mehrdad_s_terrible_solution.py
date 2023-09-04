from collections import defaultdict
n, x = (int(_) for _ in input().split())
arr = [int(_) for _ in input().split()]

result = 0
count = defaultdict(int)
for indx in range(n):
    result += count[arr[indx]]
    count[arr[indx] ^ x] += 1

print(result)