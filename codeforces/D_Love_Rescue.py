n = int(input())
str1 = input()
str2 = input()

root = {}
for char in str1:
    root[char] = char
for char in str2:
    root[char] = char

def find(x):
    if x == root[x]:
        return root[x]
    root[x] = find(root[x])
    return root[x]

result = []
def union(x, y):
    rootx, rooty = find(x), find(y)
    if rootx != rooty:
        result.append([rootx, rooty])
        root[rooty] = rootx

for i in range(n):
    x, y = str1[i], str2[i]
    union(x, y)

print(len(result))
for edge in result:
    print(*edge)