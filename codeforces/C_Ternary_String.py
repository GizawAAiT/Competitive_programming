t = int(input())
for _ in range(t):
    s = input()
    nums = [int(x) for x in s]
    ind = [-1,-1,-1]

    
    if len(set(nums))<3: 
        print(0)
        # print(set(nums))
        # print(s, nums)
    else:
        i = j = 0
        res = len(nums)
        while j<len(nums):
            while j<len(nums) and min(ind) == -1:
                ind[nums[j]-1] = j
                j+=1 
            while i<j and min(ind) != -1:
                if ind[nums[i]-1] == i:
                    ind[nums[i]-1] = -1
                i+=1
            res = min(res, (j-i)+1)

        print(res)



