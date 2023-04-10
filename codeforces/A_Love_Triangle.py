from collections import defaultdict
n = int(input())

nums = [int(_) for _ in input().split()]
dic = defaultdict(int)

flag = "NO"

for index, num in enumerate(nums):
    
    dic[index+1] = num
    if num in dic and dic[num] in dic and dic[dic[num]] == index+1:
        flag = 'YES'
        break
print(flag)