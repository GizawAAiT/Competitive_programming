n, q = (int(_) for _ in input().split())
root = {i : i for i in range(1, n+1)}
rank = {i : 0 for i in range(1, n+1)}
connected = [0 ] * n

def find(x):
    if root[x] == x:
        return x
    
    root[x] = find(root[x])
    return root[x]

def union(x, y):
    rootx, rooty = find(x), find(y)
    if rootx != rooty:
        if rank[rootx] < rank[rooty]:
            root[rooty] = rootx
        elif rank[rooty] < rank[rootx]:
            root[rootx] = rooty
        else:
            rank[rootx] += 1
            root[rooty] = rootx
def families(x, y):
    rootx, rooty = find(x), find(y)
    return 'YES' if rootx == rooty else 'NO'

for _ in range(q):
    type, a, b = (int(_) for _ in input().split())
    if type == 3: print(families(a, b))
    elif type == 2:
        left = a
        for right in range(a + 1, b + 1):
            if not (connected[left - 1] and connected[right - 1]) :
                union(left, right)
            connected[left] = 1
            left += 1

        connected[left-1] = 0
    elif type == 1:
        union(a, b)
    

