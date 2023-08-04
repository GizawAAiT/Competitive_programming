import heapq
def solve(a, s, n):
    h = []
    i = 0
    while i < n:
        heapq.heappush(h, (-a[i], i))
        s -= a[i]
        if s < 0:
            val, indx = heapq.heappop(h)
            return indx + 1 if (val != a[i]) else 0
        i += 1
    return 0
        
t = int(input())
for _ in range(t):
    n, s = (int(_) for _ in input().split())
    a = [int(_) for _ in input().split()]
    print(solve(a, s, n))

