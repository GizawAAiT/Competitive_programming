n = int(input())
t = [int(_ ) for _ in input().split()]

left = 0
right = n-1
left_sum, right_sum = 0, 0
while right>=left:
    if left_sum <= right_sum:
        left_sum += t[left]
        left += 1
    else:
        right_sum += t[right]
        right-=1
print(left,n-right-1)