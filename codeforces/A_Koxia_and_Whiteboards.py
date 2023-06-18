import heapq
t = int(input())
for _ in range(t):
    n, m = (int(_) for _ in input().split())
    a = [int(_) for _ in input().split()]
    b =  [int(_) for _ in input().split()]
    heapq.heapify(a)
    for x in b:
        heapq.heappop(a)
        heapq.heappush(a, x)
    print(sum(a))