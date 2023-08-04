n = int(input())
q = [int(_) for _ in input().split()]
m = int(input())

app = {}
for _ in range(m):
    a, b, cost = (int(_) for _ in input().split())
    if b in app:
        app[b] = min(app[b], cost)
    else:
        app[b] = cost
    
answer = sum(app.values()) if len(app) >= n - 1 else -1
print(answer)