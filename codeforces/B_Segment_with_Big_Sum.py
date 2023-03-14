n, s = (int(_) for _ in input().split())
nums = [int(_) for _ in input().split()]

left = 0

min_len = float('inf')
cur_sum = 0

for right in range(n):
    cur_sum += nums[right]
    while cur_sum - nums[left] >= s:
        cur_sum -= nums[left]
        left += 1
    if cur_sum >= s:
        min_len = min(min_len, right - left +1)
if min_len == float('inf'):
    print(-1)
else:
    print(min_len)
