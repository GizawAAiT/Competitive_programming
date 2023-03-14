from collections import defaultdict
n, k = (int(_ ) for _ in input().split())
arr = input().split()

left = 0
dic = defaultdict(int)
result = (1,1)
for right in range(len(arr)):
    dic[arr[right]] += 1
    while len(dic)>k:
        dic[arr[left]] -= 1
        if dic[arr[left]] == 0:
            del dic[arr[left]]
        left += 1
    if right -left > result[1]-result[0]:
        result = (left+1, right+1)
print(*result)