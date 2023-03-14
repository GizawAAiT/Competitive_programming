n, s = (int(_) for _ in input().split())
nums = [int(_) for _ in input().split()]

left = 0

max_len = 0
cur_sum = 0

for right in range(n):
    cur_sum+= nums[right]
    while cur_sum >s:
        cur_sum-= nums[left]
        left+=1
    max_len = max(max_len, right-left+1)
print(max_len)
