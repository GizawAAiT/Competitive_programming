t = int(input())
from collections import defaultdict
for _ in range(t):
    offset = defaultdict(int)
    n = int(input())
    arr = [int(_) for _ in input().split()]
    answer = 0
    for indx, num in enumerate(arr):
        off = num-indx
        answer += offset[off]
        offset[off] += 1
        # print(f"answer for{arr}:", answer, "dic:", offset)
    print(answer)

