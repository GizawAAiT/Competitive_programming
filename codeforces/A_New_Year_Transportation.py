from collections import defaultdict
n, target = (int(_) for _ in input().split())

a = [int(_) for _ in input().split()]
dic = defaultdict(int)

for i in range(1, n):
    dic[i] = i + a[i-1]

def dfs(r, target):
    if r == target:
        return True
    
    elif dic[r] == 0:  
        return False

    return dfs(dic[r], target)

if dfs(1, target):
    print('YES')

else:
    print("NO")