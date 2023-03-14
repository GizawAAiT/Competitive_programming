n, s = (int(_) for _ in input().split())
nums = [int(_) for _ in input().split()]

cur_sum = 0
count = 0
left = 0
for right in range(n):
    cur_sum += nums[right]
    while cur_sum > s:
        cur_sum -= nums[left]
        left += 1
    window_size = right - left + 1
    count += window_size *(window_size+1)//2
print(count)
