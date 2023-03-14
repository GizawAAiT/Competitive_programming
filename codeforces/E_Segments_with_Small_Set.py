from collections import defaultdict
n, k = (int(_) for _ in input().split())
nums = [int(_) for _ in input().split()]

left = 0
count = 0

dic = defaultdict(int)
for right in range(n):
    dic[nums[left]] +=1
    while left <= right and  len(dic) > k:
        dic[nums[left]] -= 1
        if dic[nums[left]] == 0:
            dic.pop(nums[left])
    count += right - left + 1
print(count)