t = int(input())

for _ in range(t):
    dic = {}
    n = int(input())
    nums = input().split()
    string = input()
    # print(nums,string)
    flag = 'YES'
    for i in range(n):
        if nums[i] in dic and dic[nums[i]]!=string[i]:
            flag = 'NO'
            break
        else:
            dic[nums[i]]=string[i]
    print(flag)
