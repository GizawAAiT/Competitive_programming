from collections import defaultdict
class N:
    def __init__(self, val = None,  left = None, right= None):
        self.val = val
        self.left = left
        self.right = right

def count(root, memo, dic, s):
    if root not in dic:
        return [0, 0]
    if root not in memo:
        result = [0, 0]
        if s[root] == 'W':
            result[0] += 1
        else:
            result[1] += 1
        for child in dic[root]:
            one, two = count(child, memo, dic, s)
            result[0] += one
            result[1] += two
        memo[root] = result
    return memo[root]
    
           
t = int(input())
for _ in range(t):
    n = int(input())
    nums = [int(_) for _ in input().split()]
    s = input()

    dic = defaultdict(list)
    for i in range(n-1):
        parent = nums[i]
        child = i + 2
        dic[parent].append(child)
    
    root = 1
    answer = [0]
    memo = {}
    for i in range(1, n+1):
        c = count(root, memo, dic, s)
        if c[0] == c[1]:
            answer[0] += 1
    
    print(answer[0])



    




