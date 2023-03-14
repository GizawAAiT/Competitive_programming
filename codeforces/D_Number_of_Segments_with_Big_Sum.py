n, s = (int(_) for _ in input().split())
nums = [int(_) for _ in input().split()]

count = 0
cur_sum = 0
left = 0

for right in range(n):
    cur_sum += nums[right]
    while cur_sum >= s:
        count += n-right
        cur_sum -= nums[left]
        left += 1              


print(count)
