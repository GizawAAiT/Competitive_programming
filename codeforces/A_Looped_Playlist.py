n, p = (int(_) for _ in input().split())
nums = [int(_) for _ in input().split()]

left  = 0
cur_sum = 0
min_length = float('inf')

total = sum(nums)
q = p // total
p = p%total
min_index = 0
for right in range(2*n):
    cur_sum += nums[right%n]
    while cur_sum -nums[left%n] >= p:
        cur_sum -= nums[left%n]
        left += 1
    if cur_sum >= p and right-left+1 < min_length:
        min_length = right - left +1
        min_index = left%n
print(min_index+1, min_length + q*n)

    
