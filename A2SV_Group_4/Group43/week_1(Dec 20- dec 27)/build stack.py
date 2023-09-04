# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT

T = int(input())

for _ in range(T):
    n = int(input())
    nums = [int(n) for n in input().split()]
    cur = float('inf') 
    flag = 'Yes'
    i, j = 0, len(nums)-1
    
    while i <= j:
        if nums[i]>cur or nums[j]>cur: 
            flag = 'No'
            break
        elif nums[i]>=nums[j]:
            cur = nums[i]
            i+=1
        else:
            cur = nums[j]
            j-=1
    print(flag)
    
            

