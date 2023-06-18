n, m = (int(_) for _ in input().split())

root = {i : i for i in range(1, n+1)}
rank = {i : 1 for i in range(1, n+1)}
count = {i : 1 for i in range(1, n+1)}

def find(x):
    while x != root[x]:
        x = root[x]
    return x

def union(x, y):
    rootx, rooty = find(x), find(y)
    countx, county = count[rootx], count[rooty]
    if rootx != rooty:
        if rank[rootx] > rank[rooty]:
            root[rooty] = rootx
        elif rank[rooty] > rank[rootx]:
            root[rootx] = rooty
            
        else:
            rank[rootx] += 1
            root[rooty] = rootx
        count[rootx] += county
        count[rooty] += countx
for i in range(m):
    friends = [int(_) for _ in input().split()]
    left = 1
    if len(friends) > 2:
        for right in range(2, len(friends) ):
            union(friends[left], friends[right])
        # left += 1

result = []   
for x in range(1, n+1):
    result.append(count[root[x]])
    # print(root[x])
print(*result)