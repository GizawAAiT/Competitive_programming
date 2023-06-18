n, m = (int(_) for _ in input().split())
nums = [int(_) for _ in input().split()]
minimum = 0
for i in range(n):
    if nums[i] < nums[minimum]:
        minimum = i
        break


connections = []
for _ in range(m):
    x, y, w = (int(_) for _ in input().split())
    connections.append((x, y, w))

for i in range(n):
    if i != minimum:
        connections.append((i + 1, minimum + 1, nums[i] + nums[minimum]))
connections.sort(key = lambda i: i[2])

root = {i : i for i in range(1, n+1)}

def find(x):
    if x == root[x]:
        return root[x]
    root[x] = find(root[x])
    return root[x]

result = [0]
def union(x, y, w):
    rootx, rooty = find(x), find(y)
    if rootx != rooty:
        result[0] += w
        root[rooty] = rootx

for x, y, w in connections:
    union(x, y, w)

print(result[0])